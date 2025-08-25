# -*- coding: utf-8 -*-
"""
Custom authentication views with Swagger documentation
"""

from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)


class CustomTokenObtainPairView(TokenObtainPairView):
    """JWT token obtain view with Swagger documentation"""

    @swagger_auto_schema(
        tags=["Authentication"],
        operation_description="Obtener token JWT para autenticación",
        operation_summary="Login de administrador",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    """JWT token refresh view with Swagger documentation"""

    @swagger_auto_schema(
        tags=["Authentication"],
        operation_description="Refrescar token JWT expirado",
        operation_summary="Refresh de token",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenBlacklistView(TokenBlacklistView):
    """JWT token blacklist view with Swagger documentation"""

    @swagger_auto_schema(
        tags=["Authentication"],
        operation_description="Invalidar token JWT (logout)",
        operation_summary="Logout de administrador",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
