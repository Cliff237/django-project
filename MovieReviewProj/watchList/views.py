from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from movies.models import Movie

def add_to_watchList(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    
    if 'watchList' not in request.session:
        request.session['watchList'] = []
    
    watchList = request.session['watchList']
    
    if movie.id not in watchList:
        watchList.append(movie.id)
        request.session.modified = True
        messages.success(request, f"✅ {movie.title} added to Watchlist")
    else:
        messages.info(request, f"{movie.title} is already in your Watchlist")
    
    return redirect('movies:movie_detail', slug=movie_slug)


def remove_from_watchList(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    
    if 'watchList' in request.session:
        watchList = request.session['watchList']
        if movie.id in watchList:
            watchList.remove(movie.id)
            request.session.modified = True
            messages.success(request, f"🗑️ {movie.title} removed from Watchlist")
    
    return redirect('watchList:watchlist_view')


def clear_watchList(request):
    if 'watchList' in request.session:
        request.session['watchList'] = []
        request.session.modified = True
    messages.success(request, "Watchlist cleared successfully")
    return redirect('watchList:watchlist_view')


def watchList_view(request):
    movie_ids = request.session.get('watchList', [])
    movies = Movie.objects.filter(id__in=movie_ids).order_by('-release_date')
    
    context = {
        'movies': movies,
        'watchlist_count': len(movie_ids),
    }
    return render(request, 'watchList/watchList.html', context)