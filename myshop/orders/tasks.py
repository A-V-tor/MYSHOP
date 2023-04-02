import json

from celery import shared_task
import os

from django.contrib.auth import get_user_model
from django.utils import timezone
from django_celery_beat.models import PeriodicTask
from django.core.mail import EmailMessage

from users.token import token_generated
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from yookassa import Payment, Configuration
from dotenv import load_dotenv, find_dotenv
from product.models import Product
from orders.models import Order, StateCart
from .other import restoring_stock

load_dotenv(find_dotenv())


@shared_task(name='get_status_order')
def get_status_order(payment_id, order, state):
    """Отслеживание статуса заказа,

    снятие задачи в случаях отмены

    или оплаты
    """

    # настройки магазина
    Configuration.configure(os.getenv('id_shop'), os.getenv('key_api'))

    # текущий платеж
    res = Payment.find_one(payment_id)

    date_pay = json.loads(res.json())['created_at']

    # преобразование строки в формат времени utc +3
    valid_date_pay = datetime.fromisoformat(date_pay[:-1]) + timedelta(hours=3)

    # если товар оплачен снимается задача
    if json.loads(res.json())['status'] == 'succeeded':
        order = Order.objects.get(pk=order)
        order.status = 'оплачено'
        order.date_updated = timezone.now()
        order.save()
        task = PeriodicTask.objects.get(name=f'заказ №{order}')
        task.enabled = False
        task.save()

    # если прошло больше 10 минут , снимается задача
    if datetime.now() > valid_date_pay + timedelta(minutes=10):
        order = Order.objects.get(pk=order)
        order.status = 'отменен'
        order.date_updated = timezone.now()
        order.save()
        data = StateCart.objects.get(id=state)

        restoring_stock(data, Product)

        task = PeriodicTask.objects.get(name=f'заказ №{order}')
        task.enabled = False
        task.save()


@shared_task
def send_message_by_user_email(pk):
    """Отправка сообщения с сылкой для подтверждения почты."""
    User = get_user_model()
    user = User.objects.get(pk=pk)
    mail_subject = 'Подтверждение электронной почты'
    message = render_to_string(
        'orders/verifed_email.html',
        {
            'user': user,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': token_generated.make_token(user),
        },
    )

    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()

