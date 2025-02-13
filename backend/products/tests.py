from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Products, Category


class ProductTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test description')
        self.product = Products.objects.create(
            name='Test Product',
            description='Test product description',
            price=10.00,
            category = self.category,
            materials=[],
            dimensions='10x10',
            disponibility = True,
        )
    
    def test_product_list(self):
        url = reverse('product.-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)