from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, Sex, Category


class MaleView(TemplateView):
    """Отображение категорий мужской одежды"""

    extra_context = {'title': 'мужская одежда'}
    template_name = "product/male.html"


class FemaleView(TemplateView):
    """Отображение категорий женской одежды"""

    extra_context = {'title': 'женская одежда'}
    template_name = "product/female.html"


class JeansListFemaleView(ListView):
    """Отображение женских джинс"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='woman', category__name='jeans')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'джинсы'
        context['product'] = 'Джинсы'
        return context


class JeansListMaleView(ListView):
    """Отображение мужских джинс"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='man', category__name='jeans')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'джинсы'
        context['product'] = 'Джинсы'
        return context


class ShirtListMaleView(ListView):
    """Отображение списка мужских рубашек"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='man', category__name='shirt')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'рубашки'
        context['product'] = 'Рубашки'
        return context


class ShirtListFemaleView(ListView):
    """Отображение списка женских рубашек"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='woman', category__name='shirt')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'рубашки'
        context['product'] = 'Рубашки'
        return context


class TshirtListMaleView(ListView):
    """Отображение списка мужских футболок"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='man', category__name='tshirt')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'футболки'
        context['product'] = 'Футболки'
        return context


class TshirtListFemaleView(ListView):
    """Отображение списка женских футболок"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='woman', category__name='tshirt')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'футболки'
        context['product'] = 'Футболки'
        return context


class CapListMaleView(ListView):
    """Отображение списка мужских шапок"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='man', category__name='cap')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'шапки'
        context['product'] = 'Шапки'
        return context


class CapListFemaleView(ListView):
    """Отображение списка женских шапок"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='woman', category__name='cap')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'шапки'
        context['product'] = 'Шапки'
        return context


class ScarfListMaleView(ListView):
    """Отображение списка мужских шарфов"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='man', category__name='scarf')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'шарфы'
        context['product'] = 'Шарфы'
        return context


class ScarfListFemaleView(ListView):
    """Отображение списка женских шарфов"""

    model = Product
    template_name = "product/product.html"
    queryset = Product.objects.filter(is_published=True, sex__value='woman', category__name='scarf')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'шарфы'
        context['product'] = 'Шарфы'
        return context


class ProductDetailView(DetailView):
    """Детальное отображение товара"""

    model = Product
    template_name = "product/detail-product.html"
    extra_context = {'title': 'товар'}
