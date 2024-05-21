
from operator import truediv
from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("secretkey"),

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("debugguer"),

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'core',  
    'rest_framework_simplejwt',
    'djoser',                   # Libreia implementada para todo lo que es la autenticacion del login 
    'rest_framework.authtoken', # Para crear tokens de identificacion
    'imacuna.apps.ImacunaConfig',
    'r_agrocablebot',
    'django_celery_results', #celery
    'django_celery_beat',

    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# Configuración de Channels
ASGI_APPLICATION = 'tu_proyecto.asgi.application'

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels.layers.InMemoryChannelLayer',  # Usando una capa en memoria para desarrollo
#     },
# }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')], # Directorio de las plantillas
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

WSGI_APPLICATION = 'core.wsgi.application'

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS =   ["http://localhost:8080" , "http://imacuna.com:8080"]
CSRF_ALLOWED_ORIGINS =   ["http://localhost:8080" , "http://imacuna.com:8080"]
CORS_ORIGINS_WHITELIST = ["http://localhost:8080" , "http://imacuna.com:8080"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("mariadb_name"),
        'USER': os.environ.get("mariadb_user"),
        'PASSWORD': os.environ.get("mariadb_password"),
        'HOST': 'localhost',
        'PORT': os.environ.get("mariadb_port"),
    }
}

CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True 

# --- Configuracion de servidor MQTT------b
MQTT_SERVER = os.environ.get("MQTT_SERVER"),
MQTT_PORT = os.environ.get("MQTT_PORT"),
MQTT_KEEPALIVE =  os.environ.get("MQTT_KEEPALIVE"),
MQTT_USER = os.environ.get("MQTT_USER"),
MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD"),

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media/')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Directorio de Vue
UI_DIR = os.path.join(BASE_DIR, 'ui/')

# Celery settings

CELERY_BROKER_URL = 'amqp://{}:{}@{}:{}'.format(
    'JuanFelipe',
    'Juanfe142228.',
    'localhost',
    '5672'
)
CELERY_FLOWER_URL = 'http://{}:{}@{}:{}'.format(
    'JuanFelipe',
    'Juanfe142228.',
    'localhost',
    '5555'
)

# Nueva configuración para controlar los intentos de conexión con el broker durante el inicio
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Bogota'
CELERY_ENABLE_UTC = True
# CELERY_BEAT_SCHEDULE = {
#     'ejecutar_evento_programado': {
#         'task': 'r_agrocablebot.tasks.ejecutar_evento_programado',
#         'schedule': timedelta(minutes=1),  # Ejecutar cada minuto
#     },
#     # 'ejecutar_evento':{
#     #     'task': 'r_agrocablebot.tasks.ejecutar_evento',
#     #     'schedule': timedelta(minutes=1),  # Ejecutar cada minuto
#     # },
#     # 'send_data_via_email':{
#     #     'task': 'r_agrocablebot.tasks.send_data_via_email',
#     #     'schedule': timedelta(minutes=2), 
#     # }
# }




# Para el envio de correos
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Cambia esto por tu servidor SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'semillero.imacuna@gmail.com'  # Tu dirección de correo
EMAIL_HOST_PASSWORD = 'dimo kagp dggc jzco'  # Tu contraseña 
DEFAULT_FROM_EMAIL = 'semillero.imacuna@gmail.com'  # La dirección desde la que se envían los correos