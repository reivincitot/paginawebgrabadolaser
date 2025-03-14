from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SocialAuthSerializer, UserSerializer
from django.contrib.auth import authenticate

class BaseSocialLogin(APIView):
    """Base class for social authentication"""
    provider = None
    user_info_url = None
    user_info_params = {}
    
    def post(self, request):
        serializer = SocialAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            # Get users data
            response = requests.get(
                self.user_info_url,
                params={**self.user_info_params, 
                        'access_token': serializer.validated_data['access_token']}
            )
            response.raise_for_status()
            user_info = response.json()
            
            # Email manage for Facebook
            email = user_info.get('email')
            if not email and self.provider == 'facebook':
                email = f"{user_info.get('id', '')}@facebook.com"
            
            # Create/Update for  user
            user, created = User.objects.update_or_create(
                email=email,
                defaults={
                    'first_name': user_info.get('first_name', ''),
                    'last_name': user_info.get('last_name', ''),
                    'social_id': user_info.get('id'),
                    'social_provider': self.provider
                }
            )
            
            # Token generation
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
            
        except requests.exceptions.HTTPError:
            return Response(
                {'error': f'Invalid {self.provider} token'},
                status=status.HTTP_400_BAD_REQUEST
            )

class GoogleLogin(BaseSocialLogin):
    provider = 'google'
    user_info_url = 'https://www.googleapis.com/oauth2/v3/userinfo'
    user_info_params = {'alt': 'json'}

class FacebookLogin(BaseSocialLogin):
    provider = 'facebook'
    user_info_url = 'https://graph.facebook.com/v19.0/me'
    user_info_params = {'fields': 'id,email,first_name,last_name'}

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfileView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    