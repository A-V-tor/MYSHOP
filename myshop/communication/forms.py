from django import forms
from .models import Feedback
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
