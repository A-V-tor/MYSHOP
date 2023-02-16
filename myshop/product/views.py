from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth import get_user_model
from orders.models import Cart
from .models import Product, Sex, Category


class MaleView(TemplateView):
    """Отображение категорий мужской одежды"""

    template_name = 'product/male.html'
    extra_context = {'title': 'мужская одежда'}


class FemaleView(TemplateView):
    """Отображение категорий женской одежды"""

    template_name = 'product/female.html'
    extra_context = {'title': 'женская одежда'}


class JeansListFemaleView(ListView):
    """Отображение женских джинс"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='woman', category__name='jeans'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'джинсы'
        context['product'] = 'Джинсы'
        return context


class JeansListMaleView(ListView):
    """Отображение мужских джинс"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='man', category__name='jeans'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'джинсы'
        context['product'] = 'Джинсы'
        return context


class ShirtListMaleView(ListView):
    """Отображение списка мужских рубашек"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='man', category__name='shirt'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'рубашки'
        context['product'] = 'Рубашки'
        return context


class ShirtListFemaleView(ListView):
    """Отображение списка женских рубашек"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='woman', category__name='shirt'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'рубашки'
        context['product'] = 'Рубашки'
        return context


class TshirtListMaleView(ListView):
    """Отображение списка мужских футболок"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='man', category__name='tshirt'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'футболки'
        context['product'] = 'Футболки'
        return context


class TshirtListFemaleView(ListView):
    """Отображение списка женских футболок"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='woman', category__name='tshirt'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'футболки'
        context['product'] = 'Футболки'
        return context


class CapListMaleView(ListView):
    """Отображение списка мужских шапок"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='man', category__name='cap'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'шапки'
        context['product'] = 'Шапки'
        return context


class CapListFemaleView(ListView):
    """Отображение списка женских шапок"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='woman', category__name='cap'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'шапки'
        context['product'] = 'Шапки'
        return context


class ScarfListMaleView(ListView):
    """Отображение списка мужских шарфов"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='man', category__name='scarf'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'шарфы'
        context['product'] = 'Шарфы'
        return context


class ScarfListFemaleView(ListView):
    """Отображение списка женских шарфов"""

    template_name = 'product/product.html'
    model = Product
    queryset = Product.objects.filter(
        is_published=True, sex__value='woman', category__name='scarf'
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'шарфы'
        context['product'] = 'Шарфы'
        return context


class ProductDetailView(DetailView):
    """Детальное отображение товара"""

    template_name = 'product/detail-product.html'
    model = Product
    extra_context = {'title': 'товар'}

    def post(self, request, *args, **kwargs):

        if 'size' in request.POST:
            # размер и остаток
            (size, value_size) = request.POST['size'].split(',')

            # если есть остаток, товар добавляется в корзину
            if int(value_size) > 0:
                product = self.get_object()
                user = request.user
                Cart.objects.create(
                    user_id=user, product_id=product, size=size
                )
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f'Товар {product}  {size} добавлен в корзину!',
                )

            # в случае если остатка нет, вывод соотвествующего сообщения
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'В данный момент товар отсутствует!',
                )

        return redirect(self.get_object())
