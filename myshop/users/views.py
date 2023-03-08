from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    """Регистрация пользователя"""

    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(LoginView):
    """Авторизация пользователя"""

    form_class = LoginUserForm
    extra_context = {'title': 'Авторизация'}
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    """Выход из аккаунта"""

    logout(request)
    return redirect('login')
