from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from customers.models import Customer
from products.models import Product
from orders.models import Order
from orders_products.models import OrderProduct

class OrderCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.customer = Customer.objects.create(name='Test Customer', email='test@google.com')
        self.product = Product.objects.create(name='Test Product', price=10.0, stock=10)
        self.url = reverse('api-order-create')

    def test_create_order_success(self):
        data = {
            'customer_id': self.customer.id,
            'datetime': '2023-10-01T12:00:00Z',
            'products': [
                {'product_id': self.product.id, 'quantity': 2}
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Order.objects.filter(customer=self.customer).exists())
        self.assertTrue(OrderProduct.objects.filter(order__customer=self.customer, product=self.product).exists())

    def test_create_order_invalid_customer(self):
        data = {
            'customer_id': 999, 
            'datetime': '2023-10-01T12:00:00Z',
            'products': [
                {'product_id': self.product.id, 'quantity': 2}
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_invalid_product(self):
        data = {
            'customer_id': self.customer.id,
            'datetime': '2023-10-01T12:00:00Z',
            'products': [
                {'product_id': 999, 'quantity': 2}  
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_missing_product_id(self):
        data = {
            'customer_id': self.customer.id,
            'datetime': '2023-10-01T12:00:00Z',
            'products': [
                {'quantity': 2}  
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)