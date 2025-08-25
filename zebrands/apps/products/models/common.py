# -*- coding: utf-8 -*-
from django.db import models


class Common(models.Model):
    """Base model for records"""

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)
    active = models.BooleanField(verbose_name="Active", default=True)

    class Meta:
        abstract = True
