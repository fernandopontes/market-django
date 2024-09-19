from django.test import TestCase
from django.urls import reverse
from products.models import Product
from products.forms import ProductForm

class ProductCreateViewTests(TestCase):

    def setUp(self):
        self.url = reverse('product-create')
        self.valid_data = {
            'name': 'Test Product',
            'price': 10.00,
            'stock': 10,
            'image': 'test.jpg',
        }
        self.invalid_data = {
            'name': '',
            'price': 10.00
        }

    def test_create_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/create.html')
        self.assertIsInstance(response.context['form'], ProductForm)

    def test_create_view_post_valid(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product-list'))
        self.assertTrue(Product.objects.filter(name='Test Product').exists())

    def test_create_view_post_invalid(self):
        response = self.client.post(self.url, data=self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/create.html')
        self.assertFalse(Product.objects.filter(name='Test Product 2').exists())