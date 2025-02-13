from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User, Client
from orders.models import Order, OrderItem
from products.models import Products, Category


class OrderTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='client1', password='Testpass123!')
        self.user.is_active = True
        self.user.save()
        self.client_obj = Client.objects.create(user=self.user, direction='Test Street', preferred_lenguage='en')
        self.category = Category.objects.create(name='Test Category', description='Test category')
        self.product = Products.objects.create(
            name = 'Test Product',
            description = 'Test product',
            price = 20.00,
            category = self.category,
            materials=[],
            dimensions = '10x10',
            disponibility = True,
        )
        self.client.force_authenticate(user=self.user)
        
    def test_create_order(self):
        url = reverse('order-list')
        data = {
            'shipping_direcction': 'Test Street 123',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
