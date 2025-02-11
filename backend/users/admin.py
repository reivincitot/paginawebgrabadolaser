from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from products.models import Products


admin_group, _= Group.objects.get_or_create(name="Admin")
seller_group,_= Group.objects.get_or_create(name="Vendedor")

# Get the product model for assigning permissions
product_ct= ContentType.objects.get_for_model(Products)

# Define the permissions for each group
seller_permissions = Permission.objects.filter(codename__in=["add_products","change_products"])
admin_permissions = Permission.objects.filter(codename__in=["add_products","change_products","delete_products"])

# Assign the permissions to the groups
seller_group.permissions.set(seller_permissions)
admin_group.permissions.set(admin_permissions)
