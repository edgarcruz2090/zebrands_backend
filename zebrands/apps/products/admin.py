from django.contrib import admin
from apps.products.models.brand import Brand
from apps.products.models.product import Product
from apps.products.models.track_product import TrackProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin View for Product"""

    list_display = ("name", "sku", "brand", "price", "created_at")
    list_filter = ("created_at", "active", "brand")
    readonly_fields = ("created_at", "updated_at")
    search_fields = ("name", "sku", "brand__name")
    fields = ("name", "sku", "brand", "price", "active", "created_at", "updated_at")
    raw_id_fields = ("brand",)
    ordering = ("-created_at",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Admin View for Brand"""

    list_display = ("name", "created_at")
    list_filter = ("created_at", "active")
    readonly_fields = ("created_at", "updated_at")
    search_fields = ("name",)
    fields = ("name", "active", "created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(TrackProduct)
class TrackProductAdmin(admin.ModelAdmin):
    """Admin View for TrackProduct"""

    list_display = ("product", "created_at")
    list_filter = ("created_at", "product__brand__name")
    readonly_fields = ("created_at", "updated_at")
    search_fields = ("product__name", "created_at")
    fields = ("product", "active", "created_at", "updated_at")
    raw_id_fields = ("product",)
    ordering = ("-created_at",)
