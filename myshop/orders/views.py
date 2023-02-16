from django.db.models import *
from django.views.generic import ListView

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from orders.models import Cart


class CartUserView(ListView):
    """Отображение корзины товаров"""

    template_name = 'orders/cart.html'
    model = Cart

    def get_queryset(self):
        return Cart.objects.filter(user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CartUserView, self).get_context_data(**kwargs)
        user = self.request.user

        # сумма текущей корзины
        context['sum'] = (
            Cart.objects.filter(user_id=user)
            .aggregate(Sum('product_id__price'))
            .get('product_id__price__sum')
        )
        return context

    def post(self, request, *args, **kwargs):

        product_id = request.POST.get('remove_product', None)
        if product_id is not None:
            print(int(product_id))
            entries = Cart.objects.get(id=int(product_id))
            entries.delete()
        else:
            raise ValueError('Некорректное значение!')

        return redirect('cart')
