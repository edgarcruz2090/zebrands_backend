# -*- coding: utf-8 -*-
"""
Swagger configuration for the API
"""

from drf_yasg import openapi

# Tags
SWAGGER_TAGS = [
    {
        "name": "Products",
        "description": "API endpoints for managing products in the catalog",
    },
    {"name": "Brands", "description": "API endpoints for managing product brands"},
    {
        "name": "Users",
        "description": "API endpoints for managing system users (admin only)",
    },
    {"name": "Authentication", "description": "JWT authentication endpoints"},
    {"name": "Health Check", "description": "System health and status endpoints"},
]

# Info
SWAGGER_INFO = openapi.Info(
    title="ZeBrands Catalog API",
    default_version="v1",
    description="""
    Product catalog system with admin and anonymous user roles.
    - JWT authentication
    - Product management
    - Brand management
    - Usage tracking
    - Admin user management
    """,
    contact=openapi.Contact(email="edgargdcv@gmail.com"),
    license=openapi.License(name="MIT License"),
    version="1.0.0",
)

# Settings
SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT token in format: Bearer <token>",
        }
    },
    "SECURITY": [{"Bearer": []}],
    "TAGS_SORTER": "alpha",
    "OPERATIONS_SORTER": "alpha",
    "DOC_EXPANSION": "none",
    "DEEP_LINKING": True,
    "DISPLAY_OPERATION_ID": False,
    "DEFAULT_MODEL_RENDERING": "example",
    "DEFAULT_INFO": SWAGGER_INFO,
}
