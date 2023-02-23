from django.urls import path
from django.contrib.auth.decorators import login_required
from orders.views import CartUserView, ProfileUserView

urlpatterns = [
    path('cart/', login_required(CartUserView.as_view()), name='cart'),
    path(
        'profile/', login_required(ProfileUserView.as_view()), name='profile'
    ),
]
