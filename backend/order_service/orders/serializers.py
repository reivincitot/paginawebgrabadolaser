from rest_framework import serializers
from orders.models import Order, OrderItem
from users.serializers import ClientSerializer
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id', 'client', 'date', 'status', 'shipping_direction', 'items', 'total_price']
        
    def get_total_price(self, obj):
        return obj.total_price()
