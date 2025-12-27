from random import choices
from string import ascii_letters, digits

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, verbose_name='телефон', blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True)
    country = models.CharField(max_length=75, verbose_name='страна', blank=True)
    code = models.CharField(max_length=10, verbose_name='код для верификации',
                            blank=True, null=True, default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.code:
            self.is_active = False
            symbols = ascii_letters + digits
            randoms = choices(symbols, k=10)
            new_code = ''.join(randoms)
            self.code = new_code
        super().save(*args, **kwargs)
