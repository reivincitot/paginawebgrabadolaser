from rest_framework import serializers
from reports.models import SalesReport, PaymentReport, ShippingReport


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = ['id', 'date', 'total_orders', 'total_revenue', 'total_completed_orders']
        
class PaymentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReport
        fields = ['id', 'date', 'total_payments', 'total_amount', 'failed_payments']
        
class ShippingReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShippingReport
        fields = ['id', 'date', 'total_shipments', 'delivered_shipments', 'pending_shipments' ]