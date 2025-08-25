# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from django.contrib.auth.models import User

from apps.products.models.brand import Brand
from apps.products.models.common import Common
from apps.products.constants import FIELDS_TO_REPORT
from apps.products.email import SesEmail


class Product(Common):
    """Model for products"""

    name = models.CharField(
        verbose_name="Name",
        max_length=200,
        validators=[MinLengthValidator(3, "Name must be at least 3 characters long.")],
    )
    sku = models.CharField(
        verbose_name="SKU",
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(3, "SKU must be at least 3 characters long.")],
    )
    brand = models.ForeignKey(
        Brand, verbose_name="Brand", on_delete=models.CASCADE, related_name="products"
    )
    price = models.DecimalField(
        verbose_name="Price",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01, "Price must be greater than 0.")],
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def save(self, *args, **kw):
        self.full_clean()
        self.sku = self.sku.upper().strip()
        self.name = self.name.strip()

        updated = False
        data = {}
        if self.pk is not None:
            cls = self.__class__
            old = cls.objects.get(pk=self.pk)
            new = self
            for field in cls._meta.get_fields():
                field_name = field.name
                if field_name in FIELDS_TO_REPORT and getattr(
                    old, field_name
                ) != getattr(new, field_name):
                    data[field_name] = getattr(new, field_name)
                    updated = True
        super(Product, self).save(*args, **kw)
        if updated:
            self.send_update_notification(changes=data)

    def tracking_detail(self):
        """Create a ProductTrack for the instance"""
        from .track_product import TrackProduct

        TrackProduct.objects.create(product_id=self.id)

    def send_update_notification(self, changes):
        """Send a update notification when a product is updated
        Args:
            changes dict: fields updated {'field': new_value}
        """
        admin_emails = list(
            User.objects.filter(is_superuser=True).values_list("email", flat=True)
        )
        subject = "Product updated!"
        changes = "<br>".join(
            ["<b>{}</b>: {}".format(k, v) for k, v in changes.items()]
        )
        html_content = f"""
            <html>
                <head></head>
                <body>
                <h1 style='text-align:center'>Product updated!</h1>
                <h3>{self.name}</h3>
                <strong>Changes:</strong>
                <br>
                {changes}
                </body>
            </html>
        """
        email = SesEmail(to=admin_emails, subject=subject, html_content=html_content)
        email.send()
