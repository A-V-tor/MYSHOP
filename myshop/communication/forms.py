from django import forms

from .models import Feedback, Info
from captcha.fields import CaptchaField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FeedbackForm(forms.ModelForm):
    theme = forms.ChoiceField(label='Тема обращения', choices=Feedback.THEME)
    text = forms.CharField(
        label='Текст',
        widget=CKEditorUploadingWidget(),
    )
    images = forms.ImageField(
        label='Фотографии',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    captcha = CaptchaField(label='Проверка')

    class Meta:
        model = Feedback
        fields = [
            'theme',
            'text',
            'images',
        ]


class FeedbackAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = Feedback
        fields = '__all__'


class InfoAdminForm(forms.ModelForm):
    description = forms.CharField(
        label='Текст', widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Info
        fields = '__all__'
