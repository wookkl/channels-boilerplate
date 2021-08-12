import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'project.settings.storages.StaticStorage'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
DEFAULT_FILE_STORAGE = 'project.settings.storages.MediaStorage'

LOGGING_PATH = os.getenv('LOG_PATH', '/var/log/django')

# sentry
sentry_sdk.init(
    dsn="{{ sentry dsn }}",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
