from django.db import models

from django.utils import timezone


class Feedback(models.Model):
    THEME = [
        ('удаление личных данных', 'удаление личных данных'),
        ('проблема с аккаунтом', 'проблема с аккаунтом'),
        ('пожелания', 'пожелания'),
        ('некачественный товар', 'некачественный товар'),
        ('другое', 'другое'),
    ]
    STATUS = [
        ('новое', 'новое'),
        ('открыто', 'открыто'),
        ('прочитано', 'прочитано'),
    ]
    user = models.ForeignKey(
        'users.User',
        related_name='user_feedback',
        on_delete=models.SET_NULL,
        verbose_name='пользователь',
        null=True,
        blank=True,
    )
    datetime = models.DateField(
        default=timezone.now,
        verbose_name='дата',
        blank=True,
    )
    theme = models.CharField(
        choices=THEME,
        max_length=150,
        verbose_name='тема обращения',
    )
    status = models.CharField(
        choices=STATUS,
        default='новое',
        max_length=150,
        blank=True,
        verbose_name='статус',
    )
    text = models.CharField(
        max_length=255,
        verbose_name='Текст',
    )

    def __str__(self):
        return f'{self.user} - {self.theme} - {self.status}'

    def __repr__(self):
        return self.__dict__

    class Meta:
        verbose_name = 'тело записи'
        verbose_name_plural = 'Записи'


class ImageFeedback(models.Model):
    feedback = models.ForeignKey(
        'Feedback',
        related_name='images',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='запись',
    )
    image = models.ImageField(
        upload_to='feedback/%Y/%m/%d',
        blank=True,
        null=True,
        verbose_name='изображение',
    )

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'Изображения'
