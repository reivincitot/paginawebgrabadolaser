from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class AuthTests(APITestCase):
    
    def test_registration(self):
        url = reverse('auth-register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'phone_number': '123456789',
            'password': 'Testpass123!',
            'password': 'Testpass123!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(),1)
        user = User.objects.get(username='testuser')

    def test_login(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='Testpass123!')
        user.is_active = True
        user.save()
        url = reverse('auth-login')
        data = {'username': 'testuser', 'password': 'Testpass123!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        
    def test_password_reset_request(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='Testpass123')
        user.is_active = True
        user.save()
        url = reverse('password-reset-request')
        data = {'email': 'test@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Password reset link has been sent', response.data['message'])