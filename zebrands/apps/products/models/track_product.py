# -*- coding: utf-8 -*-
"""
TrackProduct model for tracking product queries
"""

from django.db import models

from apps.products.models.common import Common
from apps.products.models.product import Product


class TrackProduct(Common):
    """Model for tracking product queries"""

    product = models.ForeignKey(
        Product, related_name="tracks", on_delete=models.CASCADE
    )

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "created_at",
                ]
            ),
        ]

    def __str__(self):
        return self.product.name
