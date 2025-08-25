# -*- coding: utf-8 -*-
"""
Product views for the catalog API
"""

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from apps.products.models.product import Product
from apps.products.serializers.v1.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    """Product CRUD ModelViewSet"""

    serializer_class = ProductSerializer
    permission_classes_by_action = {
        "create": [IsAuthenticated],
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "destroy": [IsAuthenticated],
        "update": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
    }

    def get_swagger_tags(self):
        return ["Products"]

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @swagger_auto_schema(
        tags=["Products"],
        operation_description="List all active products",
        operation_summary="List products",
        manual_parameters=[
            openapi.Parameter(
                "name",
                openapi.IN_QUERY,
                description="Filter by name",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Products"],
        operation_description="Get details of a specific product",
        operation_summary="Get product",
    )
    def retrieve(self, request, pk):
        product = self.get_object()
        serializer = self.get_serializer(product)
        if request.user.is_anonymous:
            product.tracking_detail()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Products"],
        operation_description="Create a new product",
        operation_summary="Create product",
    )
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        tags=["Products"],
        operation_description="Update a product completely",
        operation_summary="Update product",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Products"],
        operation_description="Update a product partially",
        operation_summary="Update product partially",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Products"],
        operation_description="Delete a product",
        operation_summary="Delete product",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
