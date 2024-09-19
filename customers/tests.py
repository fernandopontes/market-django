from django.test import TestCase
from django.urls import reverse
from customers.models import Customer
from customers.forms import CustomerForm

class CustomerCreateViewTests(TestCase):

    def setUp(self):
        self.url = reverse('customer-create')
        self.valid_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
        }
        self.invalid_data = {
            'name': '',
            'email': 'invalid-email',
        }

    def test_create_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/create.html')
        self.assertIsInstance(response.context['form'], CustomerForm)

    def test_create_view_post_valid_data(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('customer-list'))
        self.assertTrue(Customer.objects.filter(email='john.doe@example.com').exists())

    def test_create_view_post_invalid_data(self):
        response = self.client.post(self.url, data=self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/create.html')
        self.assertFalse(Customer.objects.filter(email='invalid-email').exists())