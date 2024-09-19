from django.test import TestCase, Client
from django.urls import reverse
from orders.models import Order
from customers.models import Customer
from products.models import Product
from orders_products.models import OrderProduct

class OrderCreateViewsTest(TestCase):
    def setUp(self):
        self.url = reverse('order-create')
        self.client = Client()
        self.customer = Customer.objects.create(name="Test Customer")
        self.product1 = Product.objects.create(name="Product 1", price=10.0, stock=10)
        self.product2 = Product.objects.create(name="Product 2", price=20.0, stock=5)
        self.order = Order.objects.create(customer=self.customer, date='2023-01-01 21:00:00-03')

    def test_create_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/create.html')
        self.assertIn('customers', response.context)

    def test_create_view_post(self):
        response = self.client.post(self.url, {
            'customer': self.customer.id,
            'date': '2023-01-01 21:00:00-03'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Order.objects.filter(customer=self.customer).exists())

    def test_create_order_products_view_get(self):
        response = self.client.get(reverse('order-products', kwargs={'pk': self.order.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/create-order-products.html')
        self.assertIn('order', response.context)

    def test_create_order_products_view_post(self):
        response = self.client.post(reverse('order-products', kwargs={'pk': self.order.id}), {
            'quantity-{}'.format(self.product1.id): 2,
            'quantity-{}'.format(self.product2.id): 3,
            'order': self.order.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(OrderProduct.objects.filter(order=self.order, product=self.product1, quantity=2).exists())
        self.assertTrue(OrderProduct.objects.filter(order=self.order, product=self.product2, quantity=3).exists())