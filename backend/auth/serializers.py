from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from users.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password', 'password2')
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        
        if User.objects.filter(phone_number=data['phone_number']).exists():
            raise serializers.ValidationError({'phone_number': 'This phone number is already in use.'})        
        return data
        
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number', ''),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=validated_data['password'],
            is_client=True,
            is_active=False,
        )
        return user
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists.")
        return value

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('No user is registered with this email address.')
        return value

class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password': 'Passwords do not match'})
        return data

class EmailConfirmationSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
