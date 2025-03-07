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

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    products = models.ManyToManyField(Products, related_name="OrderItem")
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATES, default="pending")
    shipping_direction = models.TextField()
    
    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())
    
    def __str__(self):
        product_names = ", ".join([item.product.name for item in self.items.all()])
        return f"Order {self.id} by {self.client.user.username}: {product_names}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.order.id} - {self.product.name} ({self.quantity})"