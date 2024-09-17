from django.contrib import admin

from orders_products.models import OrderProduct

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order__date', 'product__name', 'quantity']
    ordering = ['order__date', 'product__name']

admin.site.register(OrderProduct, OrderProductAdmin)
