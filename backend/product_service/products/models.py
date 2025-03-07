from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='img/products', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    materials = models.JSONField(default=list)
    dimensions = models.CharField(max_length=100)
    disponibility = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
