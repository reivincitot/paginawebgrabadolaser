from django.db import models
from transactions.models import Transaction


class Shipping(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_transit", "In Transit"),
        ("delivered", "Delivered"),
    ]

    tracking_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    carrier = models.CharField(max_length=100)
    estimated_delivery = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="shipping", blank=True, null=True)
    def __str__(self):
        return f"Shipping {self.tracking_number} - {self.status}"
