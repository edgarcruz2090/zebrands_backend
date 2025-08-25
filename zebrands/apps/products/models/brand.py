# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

from apps.products.models.common import Common


class Brand(Common):
    """Model definition for Brand."""

    name = models.CharField(
        verbose_name="Name",
        max_length=200,
        unique=True,
        validators=[
            MinLengthValidator(2, "Brand name must be at least 2 characters long.")
        ],
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        validators=[
            MinLengthValidator(
                10, "Description must be at least 10 characters long if provided."
            )
        ],
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        if self.name:
            self.name = self.name.strip()

        if self.description:
            self.description = self.description.strip()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
