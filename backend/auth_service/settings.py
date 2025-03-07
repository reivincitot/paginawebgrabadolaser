"""
Configuración del Microservicio de Autenticación
Incluye: Login, registro, perfiles y JWT
"""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('AUTH_SECRET_KEY')

DEBUG = 'True'

ALLOWED_HOSTS = ['*']

# Specifics apps for the services
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'rest_framework_simplejwt',
    'auth',
    'users',
]

# Authentication Database
DATABASES ={
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('AUTH_DB_NAME'),
        'USER': os.getenv('AUTH_DB_USER'),
        'PASSWORD': os.getenv('AUTH_DB_PASSWORD'),
        'HOST': os.getenv('AUTH_DB_HOST'),
        'PORT': os.getenv('AUTH_DB_PORT'),        
    }
}
EMAIL_HOST = os.getenv('AUTH_EMAIL_HOST')
EMAIL_PORT = os.getenv('AUTH_EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('AUTH_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('AUTH_EMAIL_HOST_PASSWORD')
EMAIL_USE_TL = os.getenv('AUTH_EMAIL_USE_TLS') == 'True'

# JWT Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Internationalization
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True

# CORS (only for development)
CORS_ALLOW_ALL_ORIGINS = True