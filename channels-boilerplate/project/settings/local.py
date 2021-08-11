from .base import *


DEBUG = True

SECRET_KEY = 'django-insecure-e@*g#!7!ovjfs0id)v_p3j&=+rc4@k71ef@aqih6(=lw&vcutp'

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
