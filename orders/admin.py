from django.contrib import admin

from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'customer']
    ordering = ['date', 'customer']

admin.site.register(Order, OrderAdmin)
