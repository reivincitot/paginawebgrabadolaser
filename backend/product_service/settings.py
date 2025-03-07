"""
Microservices Configuration of Products
Include: Catalog, Inventory, Reports
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('PRODUCTS_SECRET_KEY')

DEBUG = 'True'

ALLOWED_HOSTS = ['*']

# Services apps
INSTALLED_APPS = [
    'django.contrib.postgres',
    'rest_framework',
    'products',
    'reports',
]

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PRODUCTS_DB_NAME'),
        'USER': os.getenv('PRODUCTS_DB_USER'),
        'PASSWORD': os.getenv('PRODUCTS_DB_PASSWORD'),
        'HOST': os.getenv('PRODUCTS_DB_HOST'),
        'PORT': os.getenv('PRODUCTS_DB_PORT'),
    }
}

# Image storage
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# full-text search
SEARCH_CONFIG = {
    'DEFAULT_LANG': 'spanish',
    'USE_TRIGRAMS': True,
}

# Products pagination
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 24,
}