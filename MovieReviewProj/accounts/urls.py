from django.urls import path
from .views import AccountPageView
urlpatterns = [
path('accounts/', AccountPageView.as_view(), name='account'),
]