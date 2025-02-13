from django.db import models
from orders.models import Order

class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="transaction")
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    transaction_status = models.CharField(max_length=100, choices=TRANSACTION_CHOICES, default="pending")
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_currency = models.CharField(max_length=10, blank=True, null=True)
    transaction_method = models.CharField(max_length=100, blank=True, null=True)
    transaction_response = models.TextField(blank=True, null=True)
    shipping_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("in_transit", "In Transit"),
            ("delivered", "Delivered"),
        ],
        blank=True,
        null=True
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("completed", "Completed"),
            ("failed", "Failed"),
        ],
        blank=True,
        null=True
    )
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    shipping_carrier = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        if self.transaction_id:
            return f"Transaction {self.transaction_id} for Order {self.order.id}"
        else:
            return f"Transaction for Order {self.order.id}"
