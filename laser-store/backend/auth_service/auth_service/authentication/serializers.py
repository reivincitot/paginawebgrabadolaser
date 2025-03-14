from rest_framework import serializers
from .models import User, Profile


class SocialAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=True)
        
    def validate(self, attrs):
        return attrs
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['email', 'first_name', 'last_name', 'address', 'phone']
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'