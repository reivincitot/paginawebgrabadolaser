from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, Category, InventoryMovement
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminOrReadOnly




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filters_fields = ['category','price']
    search_fields =  ['name', 'description']
    ordering_fields = ['price', 'created_at']
    
    def perform_update(self, serializer):
        # Get previous stock quantity
        instance = serializer.instance
        previous_stock = instance.stock if instance else 0
        
        # Update product
        updated_product = serializer.save()
        
        # Only track inventory if stock changed
        if 'stock' in serializer.validated_data:
            new_stock = serializer.validated_data['stock']
            
            # Determine movement type
            if previous_stock == new_stock:
                movement_type = 'ADJUSTMENT'
            else:
                movement_type = 'UPDATE'
            
            # Create inventory movement record
            InventoryMovement.objects.create(
                product = updated_product,
                user = self.request.user if self.request.user.is_authenticated else None,
                new_quantity = new_stock,
                movement_type = movement_type,
                notes = f'API Update - {timezone.now().strftime('%y-%m-%d %H:%M')}'
            )
            
            # Check stock level and send notification
            if new_stock < 10:
                self.send_low_stock_notification(instance, new_stock)
        
        def send_low_stock_notification(self, product, current_stock):
            subject = f'Low Stock Alert: {product.name}'
            message = (f'Product { product.name} (ID: {product.id}) is running low.\n'
                        f'Current stock: { current_stock}\n'
                        f'Last updated: {timezone.now().strftime('%Y-%m-%d %H:%M')}')
            
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )