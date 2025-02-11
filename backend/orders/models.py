from django.db import models
from users.models import Client
from products.models import Products


class Order(models.Model):
    STATES =[
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("sent", "Sent"),
        ("delivered", "Delivered"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"(self.client) -(self.product) - (self.quantity)"