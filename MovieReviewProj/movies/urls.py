from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),                    # /movies/
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),    # /movies/inception/
]