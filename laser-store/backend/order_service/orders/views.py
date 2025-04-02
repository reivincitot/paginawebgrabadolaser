import logging
from django.db import transaction
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer
from .clients import product_client
from .task import update_inventory_async

logger = logging.getLogger(__name__)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.prefetch_related('items').all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']
    
    @transaction.atomic
    def perform_create(self, serializer):
        """
        Create order with atomic transaction
        validates stock and calculates commissions
        """
        items = self.request.data.get('items', [])
        total = 0.0
        commission_total = 0.0
        product_updates = []
        
        try:
            # Validate and process items
            for item in items:
                product_id = item.get('product_id')
                quantity = int(item.get('quantity', 0))
                
                if quantity <= 0:
                    raise ValidationError(
                        {'Quantity': 'must be greater than zero'}
                        )
                
                # Get product data from Product Service
                product_data = product_client.get_product_stock(product_id)
                
                # Stock validation
                if quantity > product_data.get('stock', 0):
                    raise ValidationError({
                        'product_id': f'Insufficient stock for product {product_id}'
                    })
                    
                # Price and commission validation
                unit_price = float(product_data.get('price', 0))
                commission_rate = float(product_data.get('commission_rate', 0.0))
                
                if unit_price <= 0:
                    raise ValidationError({
                        'product_id': f'Invalid price for product {product_id}'
                    })
                    
                # Calculate totals
                item_total = unit_price * quantity
                item_commission = item_total * commission_rate/100
                
                
                total += item_total
                commission_total += item_commission
                product_updates.append ((product_id, quantity))
                
        except APIException as e:
            logger.error(
                'Product service error during order creation',
                exc_info=True,
                extra={
                    'user': self.request.user.id,
                    'products': [i.get('product_id') for i in items]
                }
            )
            raise ValidationError('Error validating product information') from e
        
        # Create order 
        order = serializer.save(
            user=self.request.user,
            total=round(total, 2),
            commission=round(commission_total,2),
            status='pending'
        )
        
        # Create order items
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order,
                product_id=item['product_id'],
                quantity=item['quantity'],
                unit_price=unit_price,
                commission_rate=commission_rate,
            ) for item in items
        ])

        # Async inventory update
        try:
            update_inventory_async.delay(
                product_updates,
                self.request.user.id if self.request.user.is_authenticated else None,
            )
        except Exception as e:
            logger.error(
                'Failed to queue inventory update',
                exc_info=True,
                extra={'order_id': order.id}
            )
        
        @action(detail=True, methods=['POST'])
        def cancel(self,request, pk=None):
            """
            Cancel an order if in cancellable state
            """
            
            order = self.get_object()
            
            if order.status not in [Order.Status.PENDING, Order.Status.PROCESSING]:
                return Response(
                    {'error': 'Order cannot be cancelled in current status'},
                    status= status.HTTP_400_BAD_REQUEST
                )
                
            order.status = Order.Status.CANCELLED
            order.save(update_fields=['status'])
            
            logger.info(
                'Order cancelled',
                extra= {'order_id': order.id, 'user': request.user.id}
            )
            
            return Response({'status': 'Order cancelled successfully'})
        
        @action(detail=True, methods=['POST'])
        def process_payment(self, request, pk=None):
            """
            Initiate payment processing for the order
            """
            # TODO: Implement payment getway integration
            # Placeholder for the actual payment processing logic
            return Response(
                {'warning': 'Payment processing not implemented yet'},
                status=status.HTTP_501_NOT_IMPLEMENTED
            )