from django.urls import path
from .views import ReviewsPageView, AddReviewView, EditReviewView, DeleteReviewView
urlpatterns = [
    path('movies/reviews', ReviewsPageView.as_view(), name='reviews-list'),
    path('reviews/add/', AddReviewView.as_view(), name='reviews-add'),
    path('reviews/edit/<int:pk>/', EditReviewView.as_view(), name='reviews-edit'),
    path('reviews/delete/<int:pk>/', DeleteReviewView.as_view(), name='reviews-delete'),
]