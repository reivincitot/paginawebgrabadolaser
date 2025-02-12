from rest_framework import viewsets
from .models import SalesReport, PaymentReport, ShippingReport
from .serializers import SalesReportSerializer, PaymentReportSerializer, ShippingReportSerializers

class SalesReportViewSet(viewsets.ModelViewSet):
    queryset = SalesReport.objects.all()
    serializer_class=SalesReportSerializer
    
class PaymentReportViewSet(viewsets.ModelViewSet):
    queryset = PaymentReport.objects.all()
    serializer_class = PaymentReportSerializer
    
class ShippingReportViewset(viewsets.ModelViewSet):
    queryset = ShippingReport.objects.all()
    serializer_class = ShippingReportSerializers