import requests
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def create(self, request, *args, **kwargs):
        items = request.data.get('items', [])
        total_amount = 0
        
        # Validación básica de stock (simulada)
        for item in items:
            product_id = item.get('product_id')
            quantity = item.get('quantity')
            
            try:
                response = requests.get(
                    f'http://localhost:8001/api/products/{product_id}/'
                )
                response.raiser_for_status()
                product_data = response.json()
                
                if quantity > product_data.get('stock', 0):
                    return Response(
                        {"error": f"Stock insuficiente para el producto {product_id}"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except request.ConnectionError:
                return Response(
                    {'error': 'No se pudo conectar al servicio de productos'},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )
        
        # Crear la orden
        order = Order.objects.create(
            user_id=request.user.id if request.user.is_authenticated else 1,
            total_amount=sum(item['price'] * item['quantity'] for item in items),
            status='pending'
        )
        
        # Crear items de la orden
        order_items = [
            OrderItem(
                order=order,
                product_id=item['product_id'],
                quantity=item['quantity'],
                price=item['price']
            ) for item in items
        ]
        OrderItem.objects.bulk_create(order_items)
        
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer