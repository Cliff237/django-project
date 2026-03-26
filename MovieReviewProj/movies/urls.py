from django.urls import path
from .views import MoviesPageView
urlpatterns = [
path('movies/', MoviesPageView.as_view(), name='movie'),
]