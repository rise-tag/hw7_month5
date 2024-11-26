from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):  # Наследуемся от AbstractUser для работы с Django авторизацией
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона'
    )
    age = models.IntegerField(
        verbose_name='Возраст',
        null=True, blank=True
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Пользователи'
