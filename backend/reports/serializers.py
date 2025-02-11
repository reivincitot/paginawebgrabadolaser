from rest_framework import serializers
from reports.models import SalesReport


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        field = ['id', 'date', 'total_orders', 'total_revenue', 'total_completed_orders']