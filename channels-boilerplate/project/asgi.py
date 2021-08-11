import os

from channels.routing import get_default_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.local')

application = get_default_application()
