from django.db import models
from django.urls import reverse

from myshop.models import BaseProduct, BaseSizeProduct


class Product(BaseProduct, BaseSizeProduct):
    """Модель товара"""

    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE, verbose_name="категория")
    sex = models.ForeignKey('Sex', related_name='products', on_delete=models.CASCADE, verbose_name="пол")
    main_image = models.ImageField(
            upload_to=BaseProduct.main_path_upload_to("jeans"), verbose_name="фото"
        )
    additional_image_1 = models.ImageField(
        upload_to=BaseProduct.additional_path_upload_to("jeans"),
        null=True,
        blank=True,
        verbose_name="доп-фото 1",
    )
    additional_image_2 = models.ImageField(
        upload_to=BaseProduct.additional_path_upload_to("jeans"),
        null=True,
        blank=True,
        verbose_name="доп-фото 2",
    )

    def get_absolute_url(self):
        return reverse('detail', kwargs={'sex': self.sex, 'category': self.category, 'slug': self.slug})

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

class Sex(models.Model):
    """Модель принадлежности пола покупателя"""

    SEX_CHOICES = [
        ('man', 'man'),
        ('woman', 'woman')
    ]
    value = models.CharField(max_length=5, unique=True, choices=SEX_CHOICES)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'пол'
        verbose_name_plural = 'Пол'


class Category(models.Model):
    """Модель категорий товаров"""

    CATEGORY_CHOISES = [
        ('jeans', 'джинсы'),
        ('shirt', 'рубашки'),
        ('tshirt', 'футболки'),
        ('cap', 'шапки'),
        ('scarf', 'шарфы'),
    ]
    name = models.CharField(max_length=200, unique=True, db_index=True, choices=CATEGORY_CHOISES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категория'
