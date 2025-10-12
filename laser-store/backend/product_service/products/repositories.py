from django.db.models import F, Q
from .models import ProductBase


class ProductRepository:
    @staticmethod
    def get_by_sku(sku):
        return ProductBase.objects.filter(sku=sku).first()
    
    @staticmethod
    def list_active(filters=None, order_by='name'):
        qs = ProductBase.objects.filter(is_active=True)
        if filters:
            if 'vendor_id' in filters:
                qs = qs.filter(vendor_id=filters['vendor_id'])
            if 'query' in filters:
                qs = qs.filter(Q(name__icontains=filters['q']) | Q(description__icontains=filters['q']))
        return qs.order_by(order_by)
    
    @staticmethod
    def reserve_stock(product_id, amount):
        return ProductBase.objects.filter(id=product_id, stock__gte=F('reserved') + amount)\
            .update(reserved=F('reserved') + amount)
            
    @staticmethod
    def adjust_stock(product_id, delta):
        return ProductBase.objects.filter(id=product_id).update(stock=F('stock') + delta)
                