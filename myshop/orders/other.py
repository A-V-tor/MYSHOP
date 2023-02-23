import json
import os
from django.db import transaction
from yookassa import Configuration, Payment
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


def get_url_pay(order):
    # конфигурирование данными аккаунта
    Configuration.configure(
        os.getenv("id_shop"), os.getenv("key_api")
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
                'return_url': 'https://merchant-site.ru/return_url',
            },
            'capture': True,
            'description': f'{description}',
            'metadata': {'orderNumber': f'{order.id}'},
        }
    )

    payment_url = json.loads(res.json())['confirmation']['confirmation_url']
    return payment_url
