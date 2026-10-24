
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from movies.models import Movie


class ReviewsPageView(ListView):
    model = Review
    template_name = 'review/review.html'
    context_object_name = 'reviews'
    paginate_by = 10

    def get_queryset(self):
        return Review.objects.select_related('user', 'movie').order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a form for submitting a review (if user is authenticated)
        if self.request.user.is_authenticated:
            context['form'] = ReviewForm()
        return context


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            movie_id = request.POST.get('movie_id')
            movie = get_object_or_404(Movie, id=movie_id)
            # Check if the user has already reviewed this movie
            if Review.objects.filter(user=request.user, movie=movie).exists():
                messages.error(request, 'You have already reviewed this movie.')
                return redirect('movie-detail', slug=movie.slug)
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            messages.success(request, 'Your review has been submitted.')
            return redirect('movie-detail', slug=movie.slug)
        else:
            messages.error(request, 'Please correct the errors below.')
            return redirect('movie-detail', slug=request.POST.get('movie_slug'))


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk, user=request.user)
        form = ReviewForm(instance=review)
        return render(request, 'review/edit_review.html', {'form': form, 'review': review})

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk, user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated.')
            return redirect('movie-detail', slug=review.movie.slug)
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'review/edit_review.html', {'form': form, 'review': review})


class DeleteReviewView(LoginRequiredMixin, View):
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk, user=request.user)
        review.movie_slug = review.movie.slug  # store for redirect
        review.delete()
        messages.success(request, 'Your review has been deleted.')
        return redirect('movie-detail', slug=review.movie_slug)
