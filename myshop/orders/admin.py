from django.contrib import admin

from orders.models import Cart, Order


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'datetime',
        'user_id',
        'product_id',
    )


admin.site.register(Cart, CartAdmin)
admin.site.register(Order)
