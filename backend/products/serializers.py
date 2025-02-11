from rest_framework import serializers
from products.models import Products, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'images','category', 'materials', 'dimensions', 'disponibility']