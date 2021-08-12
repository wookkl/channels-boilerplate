from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'project.settings.storages.StaticStorage'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
DEFAULT_FILE_STORAGE = 'project.settings.storages.MediaStorage'
