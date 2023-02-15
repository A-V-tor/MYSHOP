import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель юзера"""

    discount_points = models.IntegerField(
        default=0, verbose_name='Скидочные балы'
    )
    birthday = models.DateField(
        default=datetime.datetime.now, verbose_name='день рождения'
    )
