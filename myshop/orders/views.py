
from django.views.generic import ListView

from django.contrib.auth import get_user_model
from django.shortcuts import render

from orders.models import Cart


class CartUserView(ListView):
    """Отображение корзины товаров"""

    template_name = 'orders/cart.html'
    model = Cart

    def get_queryset(self):
        return Cart.objects.filter(user_id=self.request.user)
