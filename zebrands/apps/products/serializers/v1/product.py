from rest_framework import serializers

from apps.products.models.brand import Brand
from apps.products.models.product import Product
from apps.products.serializers.v1.brand import BrandSerializer


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Brand.objects.filter(active=True), source="brand"
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "brand",
            "brand_id",
            "sku",
            "price",
            "created_at",
            "updated_at",
            "active",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_sku(self, value):
        """Additional SKU validation for API context"""
        if not value or len(value.strip()) < 3:
            raise serializers.ValidationError("SKU must be at least 3 characters long.")
        return value.strip()

    def validate_price(self, value):
        """Additional price validation for API context"""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value
