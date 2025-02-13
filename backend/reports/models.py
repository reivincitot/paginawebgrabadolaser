from django.db import models
from django.utils.timezone import now
from transactions.models import Transaction
from django.utils import timezone

from django.db import models
from django.utils.timezone import now
from transactions.models import Transaction

class SalesReport(models.Model):
    date = models.DateField(auto_now_add=True)
    total_orders = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_completed_orders = models.IntegerField(default=0)
    
    @classmethod
    def generate_daily_report(cls):
        """Create a daily sales report based on the orders made on that day"""
        today = now().date()
        # Filtrar transacciones cuya fecha sea la de hoy
        transactions = Transaction.objects.filter(transaction_date__date=today)
        total_orders = transactions.count()
        # Ahora sumamos, para cada transacción, el total de la orden basado en sus ítems.
        total_revenue = sum(
            sum(item.product.price * item.quantity for item in transaction.order.items.all())
            for transaction in transactions if transaction.order
        )
        # Contar las órdenes completadas (según payment_status y shipping_status)
        total_completed_orders = transactions.filter(
            payment_status="completed", shipping_status="delivered"
        ).count()
        
        report, created = cls.objects.get_or_create(
            date=today,
            defaults={
                'total_orders': total_orders,
                'total_revenue': total_revenue,
                'total_completed_orders': total_completed_orders,
            }
        )
        return report
    
    def __str__(self):
        return f"Sales Report for {self.date}"


    
class PaymentReport(models.Model):
    date = models.DateField(auto_now_add=True)
    total_payments = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    failed_payments = models.IntegerField(default=0)
    
    @classmethod
    def generate_daily_report(cls):
        """Create a daily payment report based on the payments made on that day"""
        today = now().date()
        transactions = Transaction.objects.filter(transaction_date__date=today)
        total_payments = transactions.count()
        total_amount = sum(
            transaction.transaction_amount or 0 for transaction in transactions
        )
        failed_payments = transactions.filter(payment_status="failed").count()
        
        report, created = cls.objects.get_or_create(
            date=today,
            defaults={
                'total_payments': total_payments,
                'total_amount': total_amount,
                'failed_payments': failed_payments
            }
        )
        return report
        
    def __str__(self):
        return f"Payment Report for {self.date}"


class ShippingReport(models.Model):
    date = models.DateField(default=timezone.now)
    total_shipments = models.IntegerField(default=0)
    delivered_shipments = models.IntegerField(default=0)
    pending_shipments = models.IntegerField(default=0)
    
    @classmethod
    def generate_daily_report(cls):
        """Create a daily sales report based on the orders made on that day"""
        today = timezone.now().date()
        transactions = Transaction.objects.filter(transaction_date__date=today)
        total_shipments = transactions.count()
        
        # Count the items in the filtered QuerySets
        delivered_shipments = transactions.filter(shipping_status='delivered').count()
        pending_shipmentes = transactions.filter(shipping_status = 'pending').count()
        
        report, created = cls.objects.get_or_create(
            date= today,
            defaults={
                'total_shipments': total_shipments,
                'delivered_shipments': delivered_shipments,
                'pending_shipments': pending_shipmentes,
            }
        )
        return report
    
    def __str__(self):
        return f'Shipping Report for {self.date}'