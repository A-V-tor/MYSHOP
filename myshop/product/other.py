from django.core.cache import cache


def make_cart_for_anonymous(user, product, size):
    """Создание корзины не авторизованного юзера."""
    data = cache.get(user)

    if data:
        data.append(
            f'{product.name},{product.main_image},{product.price},{size}'
        )

    else:
        data = [f'{product.name},{product.main_image},{product.price},{size}']

    cache.set(user, data, 3600)
