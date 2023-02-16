import datetime
from django.db import models


class Cart(models.Model):
    """Модель корзины товаров"""

    datetime = models.DateField(
        default=datetime.datetime.now, verbose_name='дата'
    )
    user_id = models.ForeignKey(
        'users.User',
        related_name='cart',
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )
    product_id = models.ForeignKey(
        'product.Product',
        related_name='cart',
        on_delete=models.CASCADE,
        verbose_name='товар',
    )
    size = models.CharField(
        max_length=5,
        verbose_name='размер',
        default='L',
    )
