from .models import ProductBase
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBase
        fields = '__all__'