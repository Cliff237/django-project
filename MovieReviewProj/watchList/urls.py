from django.urls import path
from . import views

app_name = 'watchList'

urlpatterns = [
    path('', views.watchList_view, name='watchlist_view'),
    path('add/<slug:movie_slug>/', views.add_to_watchList, name='add_to_watchlist'),
    path('remove/<slug:movie_slug>/', views.remove_from_watchList, name='remove_from_watchlist'),
    path('clear/', views.clear_watchList, name='clear_watchlist'),
]
