"""
Microservices Configuration of Orders
Include: Payments, Shipping, and Transactions
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('ORDERS_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

# Services apps
INSTALLED_APPS = [
    'django.contrib.postgres',
    'rest_framework',
    'orders',
    'payments',
    'shipping',
    'transactions',
]

# Orders Database
DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('ORDERS_SERVICE_DB_NAME'),
        'USER': os.getenv('ORDERS_SERVICE_DB_USER'),
        'PASSWORD': os.getenv('ORDERS_SERVICE_DB_PASSWORD'),
        'HOST': os.getenv('ORDERS_SERVICE_DB_HOST'),
        'PORT': os.getenv('ORDERS_SERVICE_DB_PORT'),
    }
}

# Payments Configuration (Stripe)
STRIPE_CONFIG = {
    'PUBLIC_KEY': os.getenv('ORDERS_STRIPE_PUBLIC_KEY'),
    'SECRET_KEY': os.getenv('ORDERS_STRIPE_SECRET_KEY'),
    'WEBHOOK_SECRET': os.getenv('ORDERS_STRIPE_WEBHOOK_SECRET')
}

# Shipping Configuration
SHIPPING_CONFIG = {
    'DEFAULT_CARRIER': 'chilexpress',
    'MAX_WEIGHT_KG': 15.0,
}