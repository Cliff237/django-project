
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import WatchListItem
from movies.models import Movie


class WatchListPageView(LoginRequiredMixin, ListView):
    model = WatchListItem
    template_name = 'watchList/watchList.html'
    context_object_name = 'watchlist_items'
    paginate_by = 12

    def get_queryset(self):
        return WatchListItem.objects.filter(user=self.request.user).select_related('movie')

class WatchListToggleView(LoginRequiredMixin, View):
    def post(self, request):
        movie_id = request.POST.get('movie_id')
        movie = get_object_or_404(Movie, id=movie_id)
        watchlist_item, created = WatchListItem.objects.get_or_create(
            user=request.user,
            movie=movie
        )
        if created:
            messages.success(request, f'"{movie.title}" has been added to your watchlist.')
        else:
            watchlist_item.delete()
            messages.success(request, f'"{movie.title}" has been removed from your watchlist.')
        return redirect('movie-detail', slug=movie.slug)

