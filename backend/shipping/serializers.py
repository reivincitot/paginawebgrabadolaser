from rest_framework import serializers
from shipping.models import Shipping
from transactions.serializers import TransactionSerializer


class ShippingSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(read_only=True)
    
    class Meta:
        model = Shipping
        fields = ['id', 'tracking_number', 'carrier', ' estimated_delivery', 'status', 'transaction']