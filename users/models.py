from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя.
    """
    username = None
    first_name = models.CharField(
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} - электронная почта: {self.email}.'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
