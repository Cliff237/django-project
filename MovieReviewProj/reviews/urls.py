from django.urls import path
from .views import MoviesReviewsPageView
urlpatterns = [
path('movies/reviews', MoviesReviewsPageView.as_view(), name='reviews'),
]