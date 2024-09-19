from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.serializers import OrderCreateSerializer
from orders_products.models import OrderProduct
from customers.models import Customer
from rest_framework.exceptions import ValidationError
from products.models import Product
from orders.models import Order
from django.http import HttpResponse

class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        customer_id = request.data.get('customer_id')
        if not Customer.objects.filter(id=customer_id).exists():
            raise ValidationError(f"Customer with id {customer_id} does not exist.")
        
        for product in request.data.get('products', []):
            product_id = product.get('product_id')
            if not Product.objects.filter(id=product_id).exists():
                raise ValidationError(f"Product with id {product_id} does not exist.")
        
        try:
            order = Order.objects.create(
                    customer_id=customer_id,
                    date=request.data.get('datetime')
                    )
            
            for product in request.data.get('products', []):
                if product.get('product_id') != None:
                    OrderProduct.objects.create(
                        order_id=order.id,
                        product_id=product.get('product_id'),
                        quantity=product.get('quantity')
                    )

            return HttpResponse(status=201)
        except Exception as e:
            raise ValidationError(f"An error occurred: {e}")