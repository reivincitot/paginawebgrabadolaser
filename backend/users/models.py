from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Extend Django user model to add custom fields."""

    phone_number = models.CharField(max_length=15, blank=True)
    is_cliente = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Client(models.Model):
    """Model to represent a client."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direcction = (models.CharField(blank=True),)
    preferred_lenguage = models.CharField(
        max_length=10, choices=[("es", "Spanish"), ("en", "English")], default="es"
    )

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    charge = models.CharField(
        max_length=10,
        choices=[
            ("admin", "Admin"),
            ("seller", "Seller"),
        ],
    )
    def __str__(self):
        return f"(self.user.username) - (self.charge)"
