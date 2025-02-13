from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Extend Django user model to add custom fields."""
    
    phone_number = models.CharField(max_length=15, blank=True)
    is_client = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    class Meta:
        app_label = "users"
        
    def __str__(self):
        return self.username

class Client(models.Model):
    """ Model to represent a client."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    direction = models.CharField(max_length=255, blank=True)
    is_client = models.BooleanField(default=False)
    preferred_language = models.CharField(
        max_length=10, 
        choices=[
            ("es", "Spanish"), 
            ("en", "English")
            ], 
        default="es"
        
    )

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    """ Model to represent an employee"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    charge = models.CharField(
        max_length=10,
        choices=[
            ("admin", "Admin"),
            ("seller", "Seller"),
        ],
    )
    
    def __str__(self):
        return f"{self.user.username} - {self.charge}"
