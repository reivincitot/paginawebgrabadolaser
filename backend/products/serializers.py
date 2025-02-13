from rest_framework import serializers
from products.models import Products, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(), source = 'category', write_only=True
    )

    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "description",
            "price",
            "images",
            "category",
            'category_id'
            "materials",
            "dimensions",
            "disponibility",
        ]
