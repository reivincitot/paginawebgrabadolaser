from rest_framework import serializers
from transactions.models import Transaction
from orders.serializers import OrderSerializer


class TransactionSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    
    class Meta:
        model = Transaction
        fields = [
            'id', 'order', 'transaction_date', 'transaction_id', 'transaction_status',
            'transaction_amount', 'transaction_currency', 'transaction_method',
            'transaction_response', 'shipping_status', 'shipping_carrier'
        ]