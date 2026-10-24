from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


class MoviesPageView(ListView):
    model = Movie
    template_name = 'movies/movies.html'
    context_object_name = 'movies'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        # Handle search
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        # Handle genre filter
        genre = self.request.GET.get('genre')
        if genre:
            queryset = queryset.filter(genres__slug=genre)
        # Handle year filter
        year = self.request.GET.get('year')
        if year:
            queryset = queryset.filter(release_date__year=year)
        # Handle sorting
        sort = self.request.GET.get('sort')
        if sort == 'title':
            queryset = queryset.order_by('title')
        elif sort == 'release_date':
            queryset = queryset.order_by('release_date')
        elif sort == 'rating':
            queryset = queryset.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')
        elif sort == '-rating':
            queryset = queryset.annotate(avg_rating=Avg('reviews__rating')).order_by('avg_rating')
        else:
            # Default sorting: by release date descending
            queryset = queryset.order_by('-release_date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add genres for filter dropdown
        from .models import Genre
        context['genres'] = Genre.objects.all()
        # Add years for filter dropdown (distinct years from movies)
        context['years'] = Movie.objects.dates('release_date', 'year', order='DESC')
        # Add current filters and sort for preserving in template
        context['current_query'] = self.request.GET.get('q', '')
        context['current_genre'] = self.request.GET.get('genre', '')
        context['current_year'] = self.request.GET.get('year', '')
        context['current_sort'] = self.request.GET.get('sort', '')
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get reviews for this movie
        context['reviews'] = self.object.reviews.all()
        # Calculate average rating
        from django.db.models import Avg
        avg_rating = self.object.reviews.aggregate(Avg('rating'))['rating__avg']
        context['avg_rating'] = round(avg_rating, 1) if avg_rating else 0
        context['review_count'] = self.object.reviews.count()
        # Check if the movie is in the user's watchlist
        if self.request.user.is_authenticated:
            from watchList.models import WatchListItem
            context['in_watchlist'] = WatchListItem.objects.filter(
                user=self.request.user,
                movie=self.object
            ).exists()
        else:
            context['in_watchlist'] = False
        return context