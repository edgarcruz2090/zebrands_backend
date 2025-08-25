# -*- coding: utf-8 -*-
"""
Brand views for the catalog API
"""

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from apps.products.models.brand import Brand
from apps.products.serializers.v1.brand import BrandSerializer


class BrandViewSet(ModelViewSet):
    """Brand CRUD ModelViewSet"""

    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated,)

    def get_swagger_tags(self):
        return ["Brands"]

    def get_queryset(self):
        queryset = Brand.objects.filter(active=True)
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @swagger_auto_schema(
        tags=["Brands"],
        operation_description="List all active brands",
        operation_summary="List brands",
        manual_parameters=[
            openapi.Parameter(
                "name",
                openapi.IN_QUERY,
                description="Filter by name",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Brands"],
        operation_description="Get details of a specific brand",
        operation_summary="Get brand",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Brands"],
        operation_description="Create a new brand",
        operation_summary="Create brand",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Brands"],
        operation_description="Update a brand completely",
        operation_summary="Update brand",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Brands"],
        operation_description="Update a brand partially",
        operation_summary="Update brand partially",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Brands"],
        operation_description="Delete a brand",
        operation_summary="Delete brand",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
