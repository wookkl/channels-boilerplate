from django.contrib import admin
from django.urls import path
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, authentication

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="Chat API",
            default_version='v1',
            description="",
            terms_of_service="",
            contact=openapi.Contact(email="contact@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
        authentication_classes=(authentication.SessionAuthentication,),
    )
