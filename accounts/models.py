from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = None
    is_staff = None
    first_name = models.CharField(unique=False, null=False, max_length=50)
    last_name = models.CharField(unique=False, null=False, max_length=50)
    is_seller = models.BooleanField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()