from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
import uuid
import base64


def generate_uid():
    return base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8').rstrip('=')[:12]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    """ Extend Django user model to add custom fields."""
    username = None
    email = models.EmailField(unique=True)
    uid = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        default=generate_uid
    )
    display_name = models.CharField(
        max_length=50,
        blank=True,
        help_text="Name to display in the app")
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        unique=True,
        null=True,
        error_messages={'unique': 'This phone number is already in use.'}
        )
    address = models.CharField(max_length=255, blank=True)
    country_code = models.CharField(max_length=10, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_client = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    class Meta:
        app_label = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f'{self.uid} - {self.get_full_name()}'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()
    
    def save(self, *args, **kwargs):
        self.username = None
        super().save(*args, **kwargs)

class Client(models.Model):
    """ Model to represent a client."""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="client",
        limit_choices_to={'is_client': True}
        )
    direction = models.CharField(max_length=255, blank=True)
    preferred_language = models.CharField(
        max_length=10, 
        choices=[
            ("es", "Spanish"), 
            ("en", "English")
            ], 
        default="es"    
    )

    def __str__(self):
        return f'Client: {self.user.get_full_name()}'

class Employee(models.Model):
    """ Model to represent an employee"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee",
        limit_choices_to={'is_employee': True}
        )
    charge = models.CharField(
        max_length=10,
        choices=[
            ("admin", "Admin"),
            ("seller", "Seller"),
        ],
    )
    
    def __str__(self):
        return f"Employee ({self.charge}): {self.user.get_full_name()}"


