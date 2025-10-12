from .serializers import ProductSerializer
from rest_framework import viewsets
from .models import ProductBase


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductBase.objects.filter(is_active=True)
    serializer_class = ProductSerializer
