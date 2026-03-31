from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre


def movie_list(request):
    movies = Movie.objects.all()

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        movies = movies.filter(title__icontains=search_query)

    # Filter by genre
    genre_id = request.GET.get('genre')
    if genre_id:
        movies = movies.filter(genres__id=genre_id)

    # Filter by movie type
    movie_type = request.GET.get('type')
    if movie_type:
        movies = movies.filter(movie_type=movie_type)

    genres = Genre.objects.all()

    context = {
        'movies': movies,
        'genres': genres,
        'search_query': search_query,
        'selected_genre': genre_id,
        'selected_type': movie_type,
    }
    return render(request, 'movies/movie_list.html', context)


def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    # Get related movies (same genres)
    recommendations = Movie.objects.filter(
        genres__in=movie.genres.all()
    ).exclude(id=movie.id).distinct()[:6]

    context = {
        'movie': movie,
        'recommendations': recommendations,
    }
    return render(request, 'movies/movie_detail.html', context)
