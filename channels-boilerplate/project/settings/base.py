from pathlib import Path
import os

from corsheaders.defaults import default_headers


# Run mode ('local' | 'develop' | 'production')
RUN_MODE = os.getenv('RUN_MODE')

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-e@*g#!7!ovjfs0id)v_p3j&=+rc4@k71ef@aqih6(=lw&vcutp')

BASE_DIR = Path(__file__).resolve().parent.parent

# CORS ORIGIN
CORS_ORIGIN_ALLOW_ALL = True

# CORS -> CLIENT CUSTOM HEADER 추가 시 다른 서비스에도 동일하게 추가해야 함 (chat, location, file...)
CORS_ALLOW_HEADERS = list(default_headers)  # + ['wt', 'X-CLIENT-OS', 'X-CLIENT-VERSION', 'X-CLIENT-DEVICE-ID']


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'channels',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
]
PROJECT_APPS = [
    'chat',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsPostCsrfMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

APPEND_SLASH = False

# ASGI PATH
ASGI_APPLICATION = 'project.routing.application'

WSGI_APPLICATION = 'project.wsgi.application'

# DB 세팅
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': '5432',
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

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MAX UPLOAD FILE SIZE
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB

# CHANNEL LAYER
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(os.getenv("CHANNEL_LAYER_HOST"), os.getenv("CHANNEL_LAYER_PORT"))]
        },
    },
}

# S3
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_ACL = os.getenv('AWS_DEFAULT_ACL')

# DOCS
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'jwt': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'wt'
        }
    },
    'USE_SESSION_AUTH': True,
    'LOGIN_URL': '/tothemars/login/'
}
