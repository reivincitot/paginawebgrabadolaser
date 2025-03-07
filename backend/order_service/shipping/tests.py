from django.test import TestCase
from shipping.models import Shipping
from transactions.models import Transaction
from orders.models import Order
from users.models import User, Client
from products.models import Products, Category
from django.utils import timezone

class ShippingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="shipuser", email="ship@example.com", password="Testpass123!"
        )
        self.user.is_active = True
        self.user.save()
        self.client_obj = Client.objects.create(
            user=self.user, direction="Shipping Street", preferred_language="en"
        )
        self.category = Category.objects.create(
            name="Shipping Category", description="Category for shipping"
        )
        self.product = Products.objects.create(
            name="Shipping Product",
            description="Product for shipping testing",
            price=75.00,
            category=self.category,
            materials=[],
            dimensions="15x15",
            disponibility=True
        )
        self.order = Order.objects.create(
            client=self.client_obj, shipping_direction="Shipping Street", status="pending"
        )
        from transactions.models import Transaction
        self.transaction = Transaction.objects.create(
            order=self.order,
            transaction_status="completed",
            transaction_amount=75.00,
            transaction_id="SHIPTXN123"
        )
    
    def test_shipping_pending(self):
        shipping = Shipping.objects.create(
            tracking_number="TRACK001",
            carrier="CarrierA",
            estimated_delivery=timezone.now().date(),
            status="pending",
            transaction=self.transaction
        )
        self.assertEqual(shipping.status, "pending")
        self.assertIn("TRACK001", str(shipping))
    
    def test_shipping_in_transit(self):
        shipping = Shipping.objects.create(
            tracking_number="TRACK002",
            carrier="CarrierB",
            estimated_delivery=timezone.now().date(),
            status="in_transit",
            transaction=self.transaction
        )
        self.assertEqual(shipping.status, "in_transit")
        self.assertIn("TRACK002", str(shipping))
    
    def test_shipping_delivered(self):
        shipping = Shipping.objects.create(
            tracking_number="TRACK003",
            carrier="CarrierC",
            estimated_delivery=timezone.now().date(),
            status="delivered",
            transaction=self.transaction
        )
        self.assertEqual(shipping.status, "delivered")
        self.assertIn("TRACK003", str(shipping))
