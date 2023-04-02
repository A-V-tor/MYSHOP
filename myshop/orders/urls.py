from django.urls import path
from django.contrib.auth.decorators import login_required
from orders.views import CartUserView, ProfileUserView, confirm_email

urlpatterns = [
    path('cart/', login_required(CartUserView.as_view()), name='cart'),
    path(
        'profile/', login_required(ProfileUserView.as_view()), name='profile'
    ),
    path(
        'confirm/<slug:uidb64>/<slug:token_for_check>',
        confirm_email,
        name='confirm_email',
    ),
]
