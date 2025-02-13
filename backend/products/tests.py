from django.test import TestCase
from products.models import Products, Category

class ProductModelTests(TestCase):
    def setUp(self):
        # Crear una categoría
        self.category = Category.objects.create(name="Electronics", description="Electronic devices")
        # Crear un producto
        self.product = Products.objects.create(
            name="Smartphone",
            description="A smartphone with many features",
            price=299.99,
            category=self.category,
            materials=["plastic", "glass"],
            dimensions="6x3",
            disponibility=True
        )
    
    def test_product_creation(self):
        self.assertEqual(str(self.product), "Smartphone")
        self.assertEqual(self.product.price, 299.99)
        self.assertEqual(self.product.category.name, "Electronics")
    
    def test_category_str(self):
        self.assertEqual(str(self.category), "Electronics")
    
    def test_product_update(self):
        # Actualizar precio y disponibilidad
        self.product.price = 249.99
        self.product.disponibility = False
        self.product.save()
        self.assertEqual(self.product.price, 249.99)
        self.assertFalse(self.product.disponibility)
