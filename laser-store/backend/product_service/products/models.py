from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='products/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class InventoryMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN_STOCK', 'Stock in'),
        ('OUT_STOCK', 'Stock out'),
        ('ADJUSTMENT', 'Inventory adjustment'),
        ('UPDATE', 'Manual update')
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    old_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    movement_type = models.CharField(max_length=13, choices=MOVEMENT_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.movement_type} ({self.timestamp})"