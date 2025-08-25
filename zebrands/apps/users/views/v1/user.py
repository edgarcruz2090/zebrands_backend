# -*- coding: utf-8 -*-
"""
User views for the catalog API
"""

from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User

from apps.users.serializers.v1.user import UserSerializer


class AdminUserViewSet(ModelViewSet):
    """User CRUD for admin users"""

    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = User.objects.all()

    def get_swagger_tags(self):
        return ["Users"]

    @swagger_auto_schema(
        tags=["Users"],
        operation_description="Listar todos los usuarios del sistema",
        operation_summary="Listar usuarios",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Users"],
        operation_description="Obtener detalles de un usuario específico",
        operation_summary="Ver usuario",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Users"],
        operation_description="Crear un nuevo usuario administrador",
        operation_summary="Crear usuario",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Users"],
        operation_description="Actualizar completamente un usuario",
        operation_summary="Actualizar usuario",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Users"],
        operation_description="Actualizar parcialmente un usuario",
        operation_summary="Actualizar parcialmente usuario",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Users"],
        operation_description="Eliminar un usuario",
        operation_summary="Eliminar usuario",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
