from rest_framework import serializers

from orders_products.models import OrderProduct

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'
        extra_kwargs = {field.name: {'required': False} for field in OrderProduct._meta.fields}