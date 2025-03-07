from rest_framework import serializers
from users.models import User, Client, Employee
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'uid', 'email','password','display_name',
            
            'first_name','last_name','phone_number',
            'address', 'country_code', 'birth_date',
            'is_client', 'is_employee'
            ]
        
        extra_kwargs = {
            'uid': {'read_only': True},
            'password': {'write_only': True},
            'is_client': {'read_only': True},
            'is_employee': {'read_only': True}
        }
    def validate_password(self,value):
        return make_password(value)
        
class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Client
        fields= ['user', 'direction', 'preferred_language']
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save(is_client=True)
        
        client = Client.objects.create(user=user, **validated_data)
        return client
    
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Employee
        fields = ['user', 'charge']
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save(is_employee=True)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee