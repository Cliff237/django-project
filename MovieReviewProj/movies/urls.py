from django.urls import path
from .views import MoviesPageView, MovieDetailView
urlpatterns = [
    path('movies/', MoviesPageView.as_view(), name='movies-list'),
    path('movies/<slug:slug>/', MovieDetailView.as_view(), name='movie-detail'),
]