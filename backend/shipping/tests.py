from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from shipping.models import Shipping
from orders.models import Order
from users.models import User, Client
from products.models import Products, Category


class ShippingTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='client1', password='Testpass123!')
        self.user.is_active = True
        self.user.save()
        self.client_obj = Client.objects.create(user = self.user, direction='Test Street', preferred_language='en')
        self.category = Category.objects.create(name='Test Category', description='Test cateogry')
        self.product = Products.objects.create(
            name ='Test Product',
            description = 'Test product',
            price = 20.00,
            category = self.category,
            materials = [],
            dimensions = '10x10',
            disponibility = True,
        )

    def test_shipping_list(self):
        url = reverse('shipping-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status=status.HTTP_200_OK)