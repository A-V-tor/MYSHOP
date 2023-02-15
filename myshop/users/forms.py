from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class RegisterUserForm(UserCreationForm):
<<<<<<< HEAD
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите email'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control py-4t', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля',widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
=======
    """Форрма регистрации"""

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={'class': 'form-control py-4', 'placeholder': 'Логин'}
        ),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите email',
            }
        ),
    )
    birthday = forms.DateField(
        label='День рождения',
        widget=forms.DateInput(
            attrs={'class': 'form-control py-4t', 'type': 'date'}
        ),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control py-4t', 'placeholder': 'Пароль'}
        ),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control py-4', 'placeholder': 'Пароль'}
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'birthday', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    """Форрма авторизации"""

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control py-4'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4'}),
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
        )
>>>>>>> 6f3665d (add: приложение users)
