"""
URL configuration for zebrands_catalog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path

from drf_yasg.views import get_schema_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import zebrands_catalog.api_v1 as api_v1
from .swagger_config import SWAGGER_INFO


schema_view = get_schema_view(
    SWAGGER_INFO,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class HealthCheckAPIView(APIView):
    """Health Check for the API"""

    @swagger_auto_schema(tags=["Health Check"])
    def get(self, request):
        return Response(data={"status": "Hello world!"}, status=status.HTTP_200_OK)


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Health check
    path("", HealthCheckAPIView.as_view(), name="health-check"),
    # API Authentication endpoints
    path("api/auth/", include("apps.authentication.urls")),
    # API v1 - Application endpoints
    path("api/v1/", include((api_v1, "api_v1"), namespace="api_v1")),
    # API Documentation
    re_path(
        r"^docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
