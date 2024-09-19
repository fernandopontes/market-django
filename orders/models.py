from django.db import models

from customers.models import Customer

class Order(models.Model):
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')

    def __str__(self):
        return f'{self.date} - {self.customer}'
    
