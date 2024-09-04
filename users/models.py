from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    # username = models.CharField(max_length=150, verbose_name='никнэйм', unique=True)
    email = models.EmailField(verbose_name='электронная почта', unique=True)
    avatar = models.ImageField(verbose_name='аватар', **NULLABLE, upload_to='users')
    token = models.CharField(max_length=150, verbose_name='токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
