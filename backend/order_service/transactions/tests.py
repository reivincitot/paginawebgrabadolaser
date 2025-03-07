from django.test import TestCase
from transactions.models import Transaction
from orders.models import Order
from users.models import User, Client
from products.models import Products, Category

class TransactionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="transuser", email="trans@example.com", password="Testpass123!"
        )
        self.user.is_active = True
        self.user.save()
        self.client_obj = Client.objects.create(
            user=self.user, direction="Transaction Street", preferred_language="en"
        )
        self.category = Category.objects.create(
            name="Transaction Category", description="Category for transactions"
        )
        self.product = Products.objects.create(
            name="Transaction Product",
            description="Product for transaction testing",
            price=100.00,
            category=self.category,
            materials=[],
            dimensions="20x20",
            disponibility=True
        )
        self.order = Order.objects.create(
            client=self.client_obj, shipping_direction="Transaction Street", status="pending"
        )
    
    def test_transaction_pending(self):
        transaction = Transaction.objects.create(
            order=self.order,
            transaction_status="pending",
            transaction_amount=100.00,
            transaction_id="TXNPENDING"
        )
        self.assertEqual(transaction.transaction_status, "pending")
        self.assertIn("TXNPENDING", str(transaction))
    
    def test_transaction_completed(self):
        transaction = Transaction.objects.create(
            order=self.order,
            transaction_status="completed",
            transaction_amount=100.00,
            transaction_id="TXNCOMPLETED"
        )
        self.assertEqual(transaction.transaction_status, "completed")
        self.assertIn("TXNCOMPLETED", str(transaction))
    
    def test_transaction_failed(self):
        transaction = Transaction.objects.create(
            order=self.order,
            transaction_status="failed",
            transaction_amount=100.00,
            transaction_id="TXNFAILED"
        )
        self.assertEqual(transaction.transaction_status, "failed")
        self.assertIn("TXNFAILED", str(transaction))
