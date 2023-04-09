from django.urls import path

from orders.views import CartUserView, ProfileUserView, confirm_email

urlpatterns = [
    path('cart/', CartUserView.as_view(), name='cart'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path(
        'confirm/<slug:uidb64>/<slug:token_for_check>',
        confirm_email,
        name='confirm_email',
    ),
]
