from django.urls import path
from django.contrib.auth import views as auth_views
from .views import createAccount, login_view

urlpatterns = [
    path('accounts/', createAccount, name='account'),
    path('accounts/login/', login_view, name='login'),
]