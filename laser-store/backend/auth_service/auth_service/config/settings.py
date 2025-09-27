import os
from pathlib import Path
import environ


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR.parent, '.env'))

SECRET_KEY = env('DJANGO_SECRET_KEY', default='change-me')

DEBUG = env('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS', default='127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'social_django',
    'authentication',
    'drf_spectacular',
]

AUTH_USER_MODEL = 'authentication.User'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'authentication.middleware.LoggingMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Auth Service API',
    'DESCRIPTION': 'API documentation for the Authentication Microservice',
    'VERSION': '1.0.0',
}

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT', default='5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('FACEBOOK_OAUTH2_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('FACEBOOK_OAUTH2_SECRET')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend
]

AUTH_USER_MODEL = 'authentication.User'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_USER')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

SERVICE_NAME = os.getenv('SERVICE_NAME', 'auth_service')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '''
            %(asctine)s %(levelname)s %(name)s %(message)s
            %(module)s %(pathname)s %(funcname)s %(lineno)d
            %(process)d %(thread)d %(username)s %(service_name)s
            ''',
            'datefmt': '%Y-%m-%dT%H:%:%SZ',
        }
    },
    'handlers': {
        'console': {
            'class': 'loggin.StreamHandler',
            'formatter':'json',
        },
        'file':{
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/auth_service/auth.log',
            'formatter': 'json',
            'maxBytes': 1024 * 1024 * 50, #50 MB
            'backupCount': 5,
        },
        'elasticsearch': {
            'class': 'elasticserach_logging.handlers.ElasticsearchHandler',
            'host': [os.getenv('ELASTICSEARCH_URL', 'http://elasticsearch:9200')],
            'index_name': 'auth_service_logs',
            'buffer_size': 100,
            'flush_frequency': 1, # Seconds
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
            'filters': ['context_filter'],
        },
    },
    'loggers':{
        'django':{
            'handlers': ['console', 'file', 'elasticsearch'],
            'level': os.getenv('LOG_LEVEL', 'INFO'),
        },
        'auth': {
            'handlers': ['console', 'file', 'elasticsearch'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
    'filters': {
        'context_filter': {
            '()': 'authentication.middleware.RequestContextFilter',
        }
    },
}    

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-log-context',
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CELERY_BROKER_URL = f"redis://{env('REDIS_HOST','redis')}:{env('REDIS_PORT','6379')}/0"

MONGO_URI = env('MONGO_URI', default='mongodb://mongo:27017/logs')