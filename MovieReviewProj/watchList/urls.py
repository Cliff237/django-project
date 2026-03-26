from django.urls import path
from .views import WatchListPageView
urlpatterns = [
path('watchList/', WatchListPageView.as_view(), name='watchList'),
]