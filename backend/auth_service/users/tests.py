from django.test import TestCase
from users.models import User, Client, Employee

class UserModelTests(TestCase):

    def test_create_user_and_client(self):
        # Crear usuario
        user = User.objects.create_user(
            username="testclient",
            email="client@example.com",
            password="Testpass123!",
            phone_number="123456789"
        )
        
        user.is_active = True
        user.save()
        # Crear Client relacionado
        client = Client.objects.create(user=user, direction="123 Main St", preferred_language="en")
        
        # Verificar que el usuario y el client se crearon correctamente
        self.assertEqual(str(user), "testclient")
        self.assertEqual(str(client), "testclient")
        self.assertEqual(client.preferred_language, "en")

    def test_create_employee(self):
        # Crear usuario
        user = User.objects.create_user(
            username="testemployee",
            email="employee@example.com",
            password="Testpass123!",
            phone_number="987654321"
        )
        user.is_active = True
        user.save()
        # Crear Employee relacionado
        employee = Employee.objects.create(user=user, charge="admin")
        
        # Verificar el __str__ de employee
        self.assertEqual(str(employee), "testemployee - admin")
    
    def test_user_fields_validation(self):
        # Probar que se puede crear un usuario sin teléfono (campo blank)
        user = User.objects.create_user(
            username="noteluser",
            email="notel@example.com",
            password="Testpass123!"
        )
        user.is_active = True
        user.save()
        self.assertEqual(user.phone_number, "")
