from rest_framework import serializers
from users.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required = True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'password', 'password2'
                )
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Password do not match'})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number',''),
            is_client=True,
            is_active=False,
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate_email(self, value):
        """Verify if the email already exist in the database"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exist.")
        return value
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)    
    
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    def validated_email(self,value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('No user is registered with this email address. ')
        return value
        
class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, required = True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)
    
    def validate(self, data):
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password': 'Passwords do not match'})
        return data
    
class EmailConfirmationSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()