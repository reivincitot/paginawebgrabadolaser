"""
Configuración principal del proyecto Django
"""

# ==============================================================================
# Importaciones y configuraciones iniciales
# ==============================================================================
import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured

# Cargar variables de entorno desde .env
load_dotenv()

# ==============================================================================
# Funciones auxiliares
# ==============================================================================
def get_env_variable(var_name: str, default=None) -> str:
    """Obtiene variables de entorno con validación de existencia"""
    value = os.getenv(var_name, default)
    if value is None:
        raise ImproperlyConfigured(
            f"Variable de entorno requerida no encontrada: {var_name}"
        )
    return value

# ==============================================================================
# Configuración básica de Django
# ==============================================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad y entorno
SECRET_KEY = get_env_variable('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
ALLOWED_HOSTS = ['*'] if DEBUG else get_env_variable('ALLOWED_HOSTS').split(',')

# Validación de producción
if os.getenv('ENVIRONMENT') == 'production' and not SECRET_KEY:
    raise ImproperlyConfigured("SECRET_KEY debe estar configurada en producción")

# ==============================================================================
# Configuración de aplicaciones y middlewares
# ==============================================================================
INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    
    # Local
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================================================================
# Configuración de REST Framework y JWT
# ==============================================================================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPES': ('Bearer',),
    'SIGNING_KEY': SECRET_KEY,
}

# ==============================================================================
# Configuración de CORS
# ==============================================================================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend local
]

# Solo para desarrollo - deshabilitar en producción
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True

# ==============================================================================
# Configuración de URLs y plantillas
# ==============================================================================
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ==============================================================================
# Configuración de base de datos
# ==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'HOST': get_env_variable('DB_HOST', 'localhost'),
        'PORT': get_env_variable('DB_PORT', '5432'),
    }
}

# ==============================================================================
# Configuración de autenticación y validación
# ==============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ==============================================================================
# Configuración de internacionalización y zona horaria
# ==============================================================================
LANGUAGE_CODE = 'es-cl'  # Español de Chile
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# ==============================================================================
# Configuración de archivos estáticos
# ==============================================================================
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================================================================
# Configuración de servicios externos
# ==============================================================================
SERVICE_AUTH_TOKEN = get_env_variable('SECURE_AUTH_TOKEN')
PRODUCT_SERVICE_URL = get_env_variable(
    'PRODUCT_SERVICE_URL',
    'http://product-service:8001'  # Valor por defecto para desarrollo
)
SERVICE_TIMEOUT = 5  # Tiempo de espera para conexiones externas (segundos)