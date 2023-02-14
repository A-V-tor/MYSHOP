import datetime

from django.db import models


class BaseProduct(models.Model):
    """Абстрактный класс товара"""

    name = models.CharField(max_length=55, verbose_name='имя')
    date = models.DateField(default=datetime.datetime.now, verbose_name='дата')
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='цена'
    )
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name='url'
    )
    country = models.CharField(max_length=55, verbose_name='страна')
    is_published = models.BooleanField(verbose_name='опубликовать  ?')

    def main_path_upload_to(value):
        """Путь загрузки основного изображения"""

        path = f'{value}/%m/%d'
        return path

    def additional_path_upload_to(value):
        """Путь загрузки дополнительного изображения"""

        path = f'{value}/%m/%d/other'
        return path

    def __str__(self):
        return f'{self.name}'

    class Meta:
        abstract = True


class BaseSizeProduct(models.Model):
    """Абстрактный класс размера товара"""

    S = models.IntegerField(default=0)
    M = models.IntegerField(default=0)
    L = models.IntegerField(default=0)
    XL = models.IntegerField(default=0)
    XXL = models.IntegerField(default=0)

    class Meta:
        abstract = True
