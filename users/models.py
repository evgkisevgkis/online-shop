from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, verbose_name='телефон', blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True)
    country = models.CharField(max_length=75, verbose_name='страна', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
