from django.urls import path
from .views import WatchListPageView, WatchListToggleView
urlpatterns = [
    path('watchlist/', WatchListPageView.as_view(), name='watchlist'),
    path('watchlist/toggle/', WatchListToggleView.as_view(), name='watchlist-toggle'),
]