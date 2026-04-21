from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Accounts(AbstractUser):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirm_password = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']