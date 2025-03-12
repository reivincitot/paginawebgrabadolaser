from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SocialAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=True)
    provider = serializers.CharField(required=True)
    
    def validate(self, attrs):
        return attrs
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ('id', 'email', 'first_name', 'last_name', 'social_provider')