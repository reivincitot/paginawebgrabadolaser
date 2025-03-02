from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.utils.text import slugify
from .models import User
from  rest_framework import serializers

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        email = data.get('email')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        
        # Validate unique email
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email already exists.")
        
        #Generate uniques usernames
        
        
        return super().populate_user(request, sociallogin, data)