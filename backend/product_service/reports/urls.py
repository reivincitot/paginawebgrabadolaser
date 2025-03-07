from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesReportViewSet, PaymentReportViewSet, ShippingReportViewset

router = DefaultRouter()
router.register(r'sales-reports', SalesReportViewSet)
router.register(r'payments-reports', PaymentReportViewSet)
router.register(r'Shipping-reports', ShippingReportViewset)

urlpatterns = [
    path('', include(router.urls)),
]
