import json
import os
from decimal import Decimal
from django.utils import timezone
from django.db import transaction
from yookassa import Configuration, Payment
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.core.cache import cache
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


@transaction.atomic
def check_available_stock(model, list_values):
    """Проверка и перезапись остатка в

    случае его наличия
    """
    list_for_save = []
    product = None
    size_product = None
    try:
        with transaction.atomic():
            for _ in list_values:
                # получение  товара
                name_product = _[0]
                product = model.objects.get(name=name_product)

                # проверка наличия  размера и его списание
                if product:
                    size_product = _[1]
                    check_size = getattr(product, size_product)

                    if int(check_size) > 0:
                        setattr(product, size_product, (int(check_size) - 1))
                        list_for_save.append(product)

                    # если товара меньше 1 вся транзакция откатывется
                    else:
                        raise InterruptedError('Товар отсутствует!!!')

                    # сохранение товара на каждой итерации
                    [i.save() for i in list_for_save]

    # бд примнимает первоначальное состояние, передача строки во вьюху
    except InterruptedError:
        return f'товара {product} размера {size_product} нет в наличии'


def get_description_pay(order):
    """Получение ссылки для оплаты заказа"""

    # конфигурирование данными аккаунта
    Configuration.configure(
        os.getenv('id_shop'),
        os.getenv('key_api'),
    )

    # строка описания заказа
    description = ''
    for i in order.products_note:
        description += i[0]
        description += '\n'
        description += i[1]
        description += '\n'
        description += i[2]
        description += ','
        description += '\n'

    res = Payment.create(
        {
            'amount': {'value': order.price, 'currency': 'RUB'},
            'confirmation': {
                'type': 'redirect',
                'return_url': f'http://127.0.0.1:8000/profile',
            },
            'capture': True,
            'description': f'{description}',
            'metadata': {'orderNumber': f'{order.id}'},
        }
    )

    payment_url = json.loads(res.json())
    return payment_url


def make_task_for_celery(order, payment_id, state):
    """Создание задачи для очереди задач

    отслеживания статуса платежа и времени заказа

    """

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name=f'заказ №{order.id}',
        task='get_status_order',
        args=json.dumps([payment_id, order.id, state.id]),
        start_time=timezone.now(),
    )


def restoring_stock(data, model):
    """Возвращение товарного остатка при отмене заказа"""

    for i in data.description:
        product = i[0]
        size = i[1]
        product = model.objects.get(name=product)
        check_size = getattr(product, size)
        setattr(product, size, (int(check_size) + 1))
        product.save()
    data.delete()


def get_all_sum_cart_anonymous_user(cart):
    """Сумма корзины не авторизованного юзера."""
    all_sum = 0
    for i in cart:
        all_sum += Decimal(i[2])

    return all_sum


def get_cart_for_anonymous(user):
    """Получение корзины не авторизованного юзера."""
    data_cart = cache.get(user)
    cart = []
    if data_cart:
        for i in data_cart:
            product = i.split(',')
            cart.extend([product])

    return cart
