from django.test import TestCase
from payments.models import Payment
from transactions.models import Transaction
from orders.models import Order
from users.models import User, Client
from products.models import Products, Category

class PaymentTests(TestCase):
    def setUp(self):
        # Crear usuario, cliente, categoría, producto, orden y transacción
        self.user = User.objects.create_user(
            username="payuser", email="pay@example.com", password="Testpass123!"
        )
        self.user.is_active = True
        self.user.save()
        self.client_obj = Client.objects.create(
            user=self.user, direction="Payment Street", preferred_language="en"
        )
        self.category = Category.objects.create(
            name="Test Category", description="Test category description"
        )
        self.product = Products.objects.create(
            name="Test Product",
            description="A product for payment testing",
            price=50.00,
            category=self.category,
            materials=[],
            dimensions="10x10",
            disponibility=True
        )
        self.order = Order.objects.create(
            client=self.client_obj, shipping_direction="Payment Street", status="pending"
        )
        # Crear una transacción asociada a la orden
        self.transaction = Transaction.objects.create(
            order=self.order,
            transaction_status="pending",
            transaction_amount=50.00,
            transaction_id="TXN123"
        )

    def test_payment_pending_with_transaction(self):
        # Test: Payment con transacción y estado "pending"
        payment = Payment.objects.create(
            method="paypal",
            transaction=self.transaction,
            amount=50.00,
            status="pending"
        )
        self.assertEqual(payment.status, "pending")
        self.assertIn("TXN123", str(payment))
    
    def test_payment_completed_with_transaction(self):
        # Cambiar el estado de la transacción a "completed"
        self.transaction.transaction_status = "completed"
        self.transaction.save()
        payment = Payment.objects.create(
            method="paypal",
            transaction=self.transaction,
            amount=50.00,
            status="completed"
        )
        self.assertEqual(payment.status, "completed")
        self.assertIn("TXN123", str(payment))
    
    def test_payment_failed_without_transaction(self):
        # Test: Payment sin transacción asociada y estado "failed"
        payment = Payment.objects.create(
            method="stripe",
            transaction=None,
            amount=50.00,
            status="failed"
        )
        self.assertEqual(payment.status, "failed")
        self.assertIn("no transaction yet", str(payment))
