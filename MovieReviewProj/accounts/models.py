
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class AccountsManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Accounts(AbstractUser):
    username = None  # Remove username field
    name = models.CharField(max_length=100, null=True)
    # surname = models.CharField(max_length=100)
    email = models.EmailField(
        max_length=100, unique=True, null=False, default="user@example.com")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AccountsManager()
