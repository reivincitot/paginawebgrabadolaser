from django.db import models
from transactions.models import Transaction

class Payment(models.Model):
    PAYMENT_METHODS = [
        ("credit_card", "Credit Card"),
        ("debit_card", "Debit Card"),
        ("paypal", "Paypal"),
        ("bank_transfer", "Bank Transfer"),
        ("stripe", "Stripe"),
    ]
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="payment", blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices= [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ], default= "pending")
    def __str__(self):
        if self.transaction:
            return f"Payment {self.transaction.transaction_id} - {self.status}"
        else:
            return f"Payment (no transaction yet) - {self.status}"
