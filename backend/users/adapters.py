from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        extra_data = sociallogin.account.extra_data
        email = extra_data.get('email')
        first_name = extra_data.get('given_name', '')
        last_name = extra_data.get('family_name', '')
        
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'is_client': True
            }
        )
        
        refresh = RefreshToken.for_user(user)
        sociallogin.token = {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
        
        sociallogin.user = user
        return user
    
    def pre_social_login(self, request, sociallogin):
        if sociallogin.user.is_client and not hasattr(sociallogin.user,'client'):
            Client.objects.create(user=sociallogin.user)