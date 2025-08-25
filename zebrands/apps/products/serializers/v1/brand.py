from rest_framework import serializers

from apps.products.models.brand import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name", "description", "created_at", "updated_at", "active")
        read_only_fields = ("id", "created_at", "updated_at")
