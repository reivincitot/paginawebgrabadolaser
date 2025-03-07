from rest_framework import serializers
from payments.models import Payment
from transactions.serializers import TransactionSerializer


class PaymentSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(read_only=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'method', 'transaction', 'amount', 'payment_date', 'status']
