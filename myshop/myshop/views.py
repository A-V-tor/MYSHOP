from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """Главная страница"""

    extra_context = {'title': 'Главная страница'}
    template_name = 'myshop/index.html'
