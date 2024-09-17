from django.db import models

from orders.models import Order
from products.models import Product

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='orders_products')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orders_products')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.order}: {self.product} x {self.quantity}'
