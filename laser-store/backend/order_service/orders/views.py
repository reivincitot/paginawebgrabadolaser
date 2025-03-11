import request
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def create(self, request, *args, **kwargs):
        product_service_url = "http://localhost:8001/api/products/1/"
        response = request.get(product_service_url)
        
        if response.status_code !=200:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)
    
class OrderItemViewSet(viewSet.ModelViewSet):
    queryset = Order.Objects.all()
    serializer_class = OrderItemSerializer
    