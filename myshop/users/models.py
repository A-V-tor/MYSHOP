import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель юзера"""

<<<<<<< HEAD
    discount_points = models.IntegerField(default=0, verbose_name="Скидочные балы")
    birthday = models.DateField(default=datetime.datetime.now, verbose_name="день рождения")
=======
    discount_points = models.IntegerField(
        default=0, verbose_name='Скидочные балы'
    )
    birthday = models.DateField(
        default=datetime.datetime.now, verbose_name='день рождения'
    )
>>>>>>> 6f3665d (add: приложение users)
