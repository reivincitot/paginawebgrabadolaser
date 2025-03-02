from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import base64



class User(AbstractUser):
    """ Extend Django user model to add custom fields."""
    username = models.CharField(max_length=150, unique=False, null=True, blank=True)
    uid = models.CharField(max_length=20, unique=True, editable=False, default=base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8').rstrip('=')[:12])
    
    
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, unique=True)
    
    address = models.CharField(max_length=255, blank=True)
    country_code = models.CharField(max_length=10, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_client = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    
    class Meta:
        app_label = "users"

    def __str__(self):
        return f'{self.uid} - {self.get_full_name()}'
    
    def get_display_name(self):
        return f'{self.first_name} {self.last_name}'

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
