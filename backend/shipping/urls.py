from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shipping.views import ShippingViewSet

router = DefaultRouter()
router.register(r'shippings', ShippingViewSet, basename='shipping')

urlpatterns = [
    path('',include(router.urls)),
]
