from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from users.models import User
from django.utils.translation import gettext_lazy as _


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password], 
        style={'input_type': 'password'},
        help_text='Enter your password.'
        )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        help_text='Repeat your password.'
        )
    
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password',
            'password2'
            )
        extra_kwargs = {
            'phone_number': {
                'required': False,
                'allow_blank': True},
            'email': {'help_text': _('Enter a valid email address.')}
        }
        error_messages = {
            'email': {
                'unique': _('This email is already registered')
            }
        }
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': _('Passwords do not match')})
        
        phone_number = data.get('phone_number')
        if phone_number and User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'phone_number': _('This phone number is already in use.')})    
        return data
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')
        user = User.objects.create(
            **validated_data,
            is_client=True,
            is_active=False,
        )
        user.set_password(password)
        user.save()
        
        return user
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("This email already exists."))
        return value.lower().strip()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        help_text= _('Registered email address.')
        )
    password = serializers.CharField(
        write_only=True, 
        required=True,
        style={'input_type':'password'},
        help_text= _('Your account password.')
        )

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(
        help_text= _('Enter your registered email')
    )

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('No account found with this email.'))
        return value

class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        help_text= _('New password')
        )
    new_password2 = serializers.CharField(
        write_only=True, 
        required=True,
        help_text= _('Repeat new password')
        )

    def validate(self, data):
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password': _('Passwords do not match')})
        return data

class EmailConfirmationSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
