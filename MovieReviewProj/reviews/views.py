from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from movies.models import Movie
from .models import Review
from django.db.models import Count, Q

def add_review(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)

    if request.method == 'POST':
        reviewer_name = request.POST.get('reviewer_name', 'Anonymous').strip()
        try:
            rating = int(request.POST.get('rating'))
        except (TypeError, ValueError):
            rating = 0

        comment = request.POST.get('comment', '').strip()

        if not comment:
            messages.error(request, "Please write a comment.")
            return render(request, 'reviews/add_review.html', {'movie': movie})

        if rating < 1 or rating > 5:
            messages.error(request, "Rating must be between 1 and 5 stars.")
            return render(request, 'reviews/add_review.html', {'movie': movie})

        Review.objects.create(
            movie=movie,
            reviewer_name=reviewer_name or "Anonymous",
            rating=rating,
            comment=comment
        )
        messages.success(request, "Thank you! Your review has been added.")
        return redirect('movies:movie_detail', slug=movie_slug)

    # GET request
    return render(request, 'reviews/add_review.html', {'movie': movie})


def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        reviewer_name = request.POST.get('reviewer_name', review.reviewer_name).strip()
        comment = request.POST.get('comment', '').strip()
        try:
            rating = int(request.POST.get('rating'))
        except (TypeError, ValueError):
            rating = review.rating

        if not comment:
            messages.error(request, "Please write a comment.")
            return render(request, 'reviews/edit_review.html', {'review': review})

        if rating < 1 or rating > 5:
            messages.error(request, "Rating must be between 1 and 5 stars.")
            return render(request, 'reviews/edit_review.html', {'review': review})

        review.reviewer_name = reviewer_name or "Anonymous"
        review.rating = rating
        review.comment = comment
        review.save()

        messages.success(request, "Review updated successfully.")
        return redirect('movies:movie_detail', slug=review.movie.slug)

    return render(request, 'reviews/edit_review.html', {'review': review})


def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    movie_slug = review.movie.slug
    review.delete()
    messages.success(request, "Review deleted successfully.")
    return redirect('movies:movie_detail', slug=movie_slug)

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    # Genre-based recommendations (fixed + improved)
    recommendations = Movie.objects.filter(
        genres__in=movie.genres.all()      # Share at least one genre
    ).exclude(
        id=movie.id
    ).annotate(
        common_genres=Count('genres', filter=Q(genres__in=movie.genres.all()), distinct=True)
    ).order_by(
        '-common_genres', 
        '-release_date'
    ).distinct()[:8]

    # Fallback: If no recommendations, show latest 6 movies (excluding current)
    if not recommendations.exists():
        recommendations = Movie.objects.exclude(id=movie.id).order_by('-release_date')[:6]

    context = {
        'movie': movie,
        'recommendations': recommendations,
    }
    
    return render(request, 'movies/movie_detail.html', context)