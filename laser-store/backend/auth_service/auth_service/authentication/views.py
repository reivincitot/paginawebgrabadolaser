from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import SocialAuthSerializer, UserSerializer
import requests

User = get_user_model()

class BaseSocialLogin(APIView):
    provider = None
    user_info_url = {}
    email_field = 'email'
    
    def post(self, request):
        serializer = SocialAuthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            access_token = serializer.validated_data['access_token']
            response = request.get(
                self.user_info_url,
                params = {**self.user_info_params, 'access_token': access_token}
            )
            response.raise_for_status()
            user_info = response.json()
            
            email = user_info.get(self.email_field)
            if not email and self.provider == 'facebook':
                email = f'{user_info['id']}@facebook.com'
                
            user, created = User.objects.update_or_create(
                email = email,
                defaults={
                    'first_name': user_info.get('fist_name', ''),
                    'last_name': user_info.get('last_name', ''),
                    'social_id': user_info.get('id') or user_info.get('sub'),
                    'social_provider': self.provider
                }
            )
            
            token = TokenObtainPairSerializer.get_token(user)
            return Response({
                'user': UserSerializer(user).data,
                'access': str(token.access_token),
                'refresh': str(token)
            })
            
        except request.HTTPError:
            return Response(
                {'error': f'Token de {self.provider.capitalize()} invalido'},
                status = status.HTTP_400_BAD_REQUEST
            )
            
class GoogleLogin(BaseSocialLogin):
    provider = 'google'
    user_info_url = 'https://www.googleapis.com/oauth2/v3/userinfor'
    user_info_params = {'alt':'json'}
    
class FacebookLogin(BaseSocialLogin):
    provider = 'facebook'
    user_info_url = 'https://graph.facebook.com/v12.0/me'
    user_info_params = {'fields': 'id,email,fist_name,last_name'}
    email_field = 'email'