import logging
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers
from .clients import product_client
from .models import Order, OrderItem
from .serializers import OrderSerializer
from .task import update_inventory_async

logger = logging.getLogger(__name__)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.prefetch_related('items').all()
        
    def perform_create(self, serializer):
        items = self.request.data.get('item', [])
        total = 0
        commission_total = 0
        
        # Stock and prices validation
        for item in items:
            product_id = item.get('product_id')
            quantity = item.get('quantity')
    
            try:
                product_data = product_client.get_product_stock(product_id)
                if quantity > product_data['stock']:
                    raise serializer.ValidationError(
                        f"Insufficient stock for product {product_id}"
                    )
                    
                # Get product price and commission 
                item['unite_price'] = product_data['price']
                item['commission_rate'] = product_data['commission_rate']
                
                # Calculate Totals
                total9= item['unite_price'] * quantity
                commission_total += (item['unite_price'] * quantity
                                    * item['commission_rate'] /100)
                
            except APIException as e:
                logger.error(f"Service error: {str(e)} ")
                raise serializers.ValidationError(
                    "Unable to validate product information"
                )
                
        # Create order
        order = serializer.save(user = self.request.user, total=total, commission = commission_total)
        
        # Create order items
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order,
                product_id=item['product_id'],
                quantity=item['quantity'],
                unit_price=item['unite_price'], 
                commission_rate=item['commission_rate']
                ) for item in items
            ])
        
        # Async inventory update
        update_inventory_async.delay(
            [item['product_id'] for item in items],
            self.request.user.id
        )
        
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()
        if order.status not in ['pending', 'processing']:
            return Response(
                {'error': ' Order cannot be cancelled'},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.status = 'cancelled'
        order.save()
        return Response({'status': 'Order cancelled'})

    @action(detail=True, methods=['post'])
    def process_paument(self, request, pk=None):
        #Implement payment logic strype, paypal etc
        pass