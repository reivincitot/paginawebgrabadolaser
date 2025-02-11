from rest_framework import serializers
from users.models import User, Client, Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', ' username', 'email', 'phone_number', 'is_client', 'is_employee']
        
class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Client
        fields= ['id', 'user', 'direction', 'preferred_lenguage']
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data, is_client=True)
        client = Client.objects.create(user=user, **validated_data)
        return client
    
class EmployeeSerializers(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Employee
        fields = ['id', 'user', 'charge']
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data, is_employee=True)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee