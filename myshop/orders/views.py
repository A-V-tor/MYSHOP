from django.contrib import messages
from django.contrib.auth import get_user_model

from django.db.models import *
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import ListView

from users.token import token_generated
from .tasks import send_message_by_user_email
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Cart, Order, StateCart
from product.models import Product
from .other import (
    check_available_stock,
    get_description_pay,
    make_task_for_celery,
    get_cart_for_anonymous,
    get_all_sum_cart_anonymous_user,
)


class CartUserView(ListView):
    """Отображение корзины товаров"""

    template_name = 'orders/cart.html'
    model = Cart
    extra_context = {'title': 'Корзина покупок'}
    object_list = None

    def get_queryset(self):
        try:
            return Cart.objects.filter(user_id=self.request.user)
        except TypeError:
            pass

    def get_context_data(self, **kwargs):
        context = super(CartUserView, self).get_context_data(**kwargs)
        user = self.request.user

        # сумма текущей корзины
        try:
            context['sum'] = (
                Cart.objects.filter(user_id=user)
                .aggregate(sum=Sum('product_id__price'))
                .get('sum')
            )
        except TypeError:
            user = self.request.META.get('HTTP_USER_AGENT', '')
            cart = get_cart_for_anonymous(user)
            sum_anonymous = get_all_sum_cart_anonymous_user(cart)
            context['cart'] = cart
            context['sum'] = sum_anonymous

        return context

    def post(self, request, *args, **kwargs):
        """Oтработка кнопок  удалить товар / оформить заказ"""

        product_id = request.POST.get('remove_product', None)
        make_pay = request.POST.get('order', None)
        # удаление
        if product_id:
            entries = Cart.objects.get(id=int(product_id))
            entries.delete()

        # формирование заказа
        if make_pay:
            status = 'ожидание'
            order_description = [
                (
                    i.product_id.name,
                    i.size,
                    str(i.product_id.price),
                )
                for i in self.get_queryset()
            ]
            order_price = self.get_context_data(**kwargs).get('sum')
            user = self.request.user

            # проверка остатка товара и его списание в случае наличия
            bad_check = check_available_stock(Product, order_description)
            if bad_check:
                messages.add_message(
                    request,
                    messages.ERROR,
                    bad_check,
                )
                return redirect('cart')

            # создание заказа
            order = Order.objects.create(
                status=status,
                products_note=order_description,
                price=order_price,
                user=user,
            )

            # сохранение информации для восстановления остатков при отмене заказа
            state = StateCart.objects.create(
                user=user,
                description=order_description,
                order=order,
            )

            payment = get_description_pay(order)
            url = payment['confirmation']['confirmation_url']
            payment_id = payment['id']

            # создание задачи для проверки оплаты заказа
            make_task_for_celery(order, payment_id, state)

            # очистака корзины
            list_products = self.get_queryset().all()
            list_products.delete()

            # получение ссылки на оплату
            return redirect(url)

        return redirect('cart')


class ProfileUserView(LoginRequiredMixin, ListView):
    """Отображение личного профиля с заказами"""

    login_url = '/login/'
    template_name = 'orders/profile.html'
    model = Order
    extra_context = {'title': 'Профиль'}

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user).order_by(
            '-date_created', 'status'
        )

    def post(self, request, *args, **kwargs):
        user = self.request.user.pk
        to_email = self.request.user.email

        if to_email:
            messages.add_message(
                request,
                messages.SUCCESS,
                'Ссылка для активации отправлена на ваш адрес электронной почты',
            )
            send_message_by_user_email.delay(user)
        else:
            messages.add_message(request, messages.ERROR, 'Не указан email')
        return redirect('profile')


def confirm_email(request, uidb64, token_for_check):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and not token_generated.check_token(
        user, token_for_check
    ):
        user.email_verified = True
        user.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Ваш email подтвержден!',
        )

    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Что-то пошло не так свяжитесь с администрацией сайта!',
        )
    return redirect('profile')
