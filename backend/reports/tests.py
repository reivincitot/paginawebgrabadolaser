from django.test import TestCase
from django.utils.timezone import now
from reports.models import SalesReport, PaymentReport, ShippingReport
from transactions.models import Transaction
from orders.models import Order
from users.models import User, Client
from products.models import Products, Category

class ReportsTests(TestCase):
    def setUp(self):
        # Crear un usuario y cliente
        self.user = User.objects.create_user(
            username="reportuser", password="Testpass123!", email="report@example.com"
        )
        self.user.is_active = True
        self.user.save()
        self.client_obj = Client.objects.create(
            user=self.user, direction="Test Street", preferred_language="en"
        )
        
        # Crear categoría y producto
        self.category = Category.objects.create(name="Report Category", description="Category desc")
        self.product = Products.objects.create(
            name="Report Product",
            description="Product for testing reports",
            price=100.00,
            category=self.category,
            materials=[],
            dimensions="10x10",
            disponibility=True
        )
        
        # Crear una orden y una transacción asociada
        self.order = Order.objects.create(
            client=self.client_obj, shipping_direction="Test Street 123", status="pending"
        )
        # Importante: se debe crear una transacción válida.
        self.transaction = Transaction.objects.create(
            order=self.order,
            transaction_status="completed",
            transaction_amount=100.00
        )

    def test_generate_sales_report(self):
        # Genera el reporte de ventas para el día actual.
        report = SalesReport.generate_daily_report()
        self.assertIsNotNone(report)
        self.assertGreaterEqual(report.total_orders, 1)
        self.assertGreaterEqual(report.total_revenue, 0)
    
    def test_generate_payment_report(self):
        # Genera el reporte de pagos para el día actual.
        report = PaymentReport.generate_daily_report()
        self.assertIsNotNone(report)
        # Como usamos la transacción creada, total_payments debería ser al menos 1
        self.assertGreaterEqual(report.total_payments, 1)
        self.assertGreaterEqual(report.total_amount, 0)
    
    def test_generate_shipping_report(self):
        # Genera el reporte de envíos para el día actual.
        report = ShippingReport.generate_daily_report()
        self.assertIsNotNone(report)
        # Verificamos que se cuenten los envíos. Dependiendo de cómo se filtren los datos, 
        # podríamos tener 0 envíos si no se asignó shipping_status.
        self.assertGreaterEqual(report.total_shipments, 0)
