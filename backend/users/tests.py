from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username = 'testuser',
            email = 'test@example.com',
            password = 'Testpass123!',
            phone_number = '123456789',
        )
        self.user.is_active = True
        self.user.save()
        
    def test_user_list(self):
        url = reverse('user-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        
    def test_user_detail(self):
        url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        
