import datetime
from django.utils import timezone
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


class Order(models.Model):
    """Модель заказа"""

    STATUS_CHOICES = [
        ('ожидание', 'ожидание'),
        ('оплачено', 'оплачено'),
        ('выполнен', 'выполнен'),
        ('не может быть выполнен', 'не может быть выполнен'),
        ('отменен', 'отменен'),
    ]

    date_created = models.DateTimeField(
        default=timezone.now, verbose_name='дата создания'
    )
    date_updated = models.DateTimeField(
        default=timezone.now, verbose_name='дата обновления статуса'
    )
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, verbose_name='статус'
    )
    products_note = models.JSONField(verbose_name='детали заказа')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='цена'
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='пользователь',
    )

    def __str__(self):
        return f'{self.id}'


class StateCart(models.Model):
    """ Сохранение описания корзины для отмены заказа """

    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='пользователь',
    )
    description = models.JSONField(verbose_name='детали корзины')
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='заказ',
    )
    date = models.DateTimeField(
        default=timezone.now, verbose_name='дата создания'
    )

    def __str__(self):
        return f'{self.id} {self.description} {self.user}'
