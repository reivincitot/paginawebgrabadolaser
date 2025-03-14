from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product_id','quantity', 'unit_price', 'commission_rate']
        
class OrderSerializer(serializers.ModelSerializer):    
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total', 'commission',
                'status', 'created_at','items'
                ]
        read_only_fields = ['user', 'total', 'commission', 'status']
        
    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("At least one item is required")
        return value