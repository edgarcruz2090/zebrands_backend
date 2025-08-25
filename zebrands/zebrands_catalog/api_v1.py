# -*- coding: utf-8 -*-
"""
API v1 URL Configuration
This module contains all the URL patterns for the API v1 endpoints
"""

from django.urls import path, include
import apps.products.urls_v1 as products_api_v1
import apps.users.urls_v1 as users_api_v1

urlpatterns = [
    # Products API v1 - includes both products and brands
    path("", include((products_api_v1, "products"), namespace="products")),
    # Users API v1
    path("users/", include((users_api_v1, "users"), namespace="users")),
]
