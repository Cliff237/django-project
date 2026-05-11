from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Accounts(AbstractUser):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']