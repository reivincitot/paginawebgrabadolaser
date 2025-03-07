from django.test import TestCase
from django.utils.timezone import now
from reports.models import SalesReport, PaymentReport, ShippingReport
from transactions.models import Transaction
from orders.models import Order, OrderItem
from users.models import User, Client
from products.models import Products, Category

class ReportsTests(TestCase):
    def setUp(self):
        # Configuración base: usuario, cliente, categoría, producto, orden
        self.user = User.objects.create_user(
            username="reportuser", email="report@example.com", password="Testpass123!"
        )
        self.user.is_active = True
        self.user.save()
        self.client_obj = Client.objects.create(
            user=self.user, direction="Report Street", preferred_language="en"
        )
        self.category = Category.objects.create(
            name="Report Category", description="Category for reports"
        )
        self.product = Products.objects.create(
            name="Report Product",
            description="Product for report testing",
            price=150.00,
            category=self.category,
            materials=[],
            dimensions="30x30",
            disponibility=True
        )
        self.order = Order.objects.create(
            client=self.client_obj, shipping_direction="Report Street 123", status="pending"
        )
    
    def test_generate_sales_report(self):
        
        self.order_item = OrderItem.objects.create(
            order= self.order,
            product= self.product,
            quantity= 1
        )
        # Creamos una transacción para simular una venta completada
        transaction = Transaction.objects.create(
            order=self.order,
            transaction_status="completed",
            transaction_amount=150.00,
            transaction_id="SALETXN001",
            payment_status = "completed",
            shipping_status = "delivered",   
        )
        transaction.save()
        
        report = SalesReport.generate_daily_report()
        self.assertIsNotNone(report)
        self.assertGreaterEqual(report.total_orders, 1)
        self.assertGreaterEqual(report.total_revenue, 150.00)
        self.assertGreaterEqual(report.total_completed_orders, 1)
    
    def test_generate_payment_report(self):
        # Creamos una transacción para simular un pago fallido
        transaction = Transaction.objects.create(
            order=self.order,
            transaction_status="failed",
            transaction_amount=150.00,
            transaction_id="PAYTXN001"
        )
        transaction.payment_status = "failed"
        transaction.save()
        
        report = PaymentReport.generate_daily_report()
        self.assertIsNotNone(report)
        self.assertGreaterEqual(report.total_payments, 1)
        self.assertGreaterEqual(report.failed_payments, 1)
    
    def test_generate_shipping_report(self):
        # Creamos una transacción para simular un envío en tránsito
        transaction = Transaction.objects.create(
            order=self.order,
            transaction_status="completed",
            transaction_amount=150.00,
            transaction_id="SHIPTXN001"
        )
        transaction.shipping_status = "in_transit"
        transaction.save()
        report = ShippingReport.generate_daily_report()
        self.assertIsNotNone(report)
        self.assertGreaterEqual(report.total_shipments, 1)
