from decimal import Decimal
from django.db import transaction
from .repositories import ProductRepository
from .models import ProductBase


class ProductService:
    def create_product(self, data, vendor=None):
        product = ProductBase(**data)
        product.vendor = vendor
        product.full_clean()
        product.save()
        return product
    
    @transaction.atomic
    def purchase(self,product_id, quantity):
        updated = ProductRepository.reserve_stock(product_id, quantity)
        if not updated:
            raise ValueError("Insufficient stock to reserve")