from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    theme = forms.ChoiceField(label='Theme', choices=Feedback.THEME)
    text = forms.CharField(
        label='Текст',
        widget=forms.Textarea(attrs={'name': 'body', 'rows': 10, 'cols': 35}),
    )
    images = forms.ImageField(
        label='Фотографии',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    class Meta:
        model = Feedback
        fields = [
            'theme',
            'text',
            'images',
        ]
