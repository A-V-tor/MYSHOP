from django.urls import path
from django.contrib.auth.decorators import login_required
from orders.views import CartUserView

urlpatterns = [
    path('cart/', login_required(CartUserView.as_view()), name='cart'),
]
