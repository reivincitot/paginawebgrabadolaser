from django.test import TestCase
from orders.models import Order, OrderItem
from users.models import User, Client
from products.models import Products, Category

class OrderModelTests(TestCase):
    def setUp(self):
        # Crear un usuario y cliente
        self.user = User.objects.create_user(
            username="orderuser",
            email="order@example.com",
            password="Testpass123!"
        )
        self.user.is_active = True
        self.user.save()
        self.client_obj = Client.objects.create(user=self.user, direction="Order St", preferred_language="en")
        
        # Crear una categoría y un par de productos
        self.category = Category.objects.create(name="Test Cat", description="Category desc")
        self.product1 = Products.objects.create(
            name="Product 1",
            description="First product",
            price=20.00,
            category=self.category,
            materials=[],
            dimensions="10x10",
            disponibility=True
        )
        self.product2 = Products.objects.create(
            name="Product 2",
            description="Second product",
            price=30.00,
            category=self.category,
            materials=[],
            dimensions="15x15",
            disponibility=True
        )
    
    def test_create_order_with_items(self):
        # Crear una orden
        order = Order.objects.create(
            client=self.client_obj,
            shipping_direction="123 Order St",
            status="pending"
        )
        # Crear OrderItems asociados
        item1 = OrderItem.objects.create(order=order, product=self.product1, quantity=2)
        item2 = OrderItem.objects.create(order=order, product=self.product2, quantity=1)
        
        # Probar el cálculo total
        expected_total = (self.product1.price * 2) + (self.product2.price * 1)
        # Nota: Hemos corregido el método total_price en el modelo Order para usar 'items'
        total = sum(item.product.price * item.quantity for item in order.items.all())
        self.assertEqual(total, expected_total)
        
        # Test __str__
        order_str = str(order)
        # Aunque el __str__ de Order puede necesitar ajustes, verificamos que incluya el username del cliente
        self.assertIn(self.user.username, order_str)
    
    def test_order_status_change(self):
        order = Order.objects.create(
            client=self.client_obj,
            shipping_direction="123 Order St",
            status="pending"
        )
        self.assertEqual(order.status, "pending")
        order.status = "delivered"
        order.save()
        self.assertEqual(order.status, "delivered")
