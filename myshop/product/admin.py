from django.contrib import admin
from product.models import Product, Category, Sex


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'country', 'sex', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('name', 'sex', 'is_published')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SexAdmin(admin.ModelAdmin):
    list_display = ('value',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sex, SexAdmin)
