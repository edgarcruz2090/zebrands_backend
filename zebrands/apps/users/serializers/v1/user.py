from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_superuser(
            username=validated_data.get("username"),
            password=validated_data.get("password"),
            email=validated_data.get("email"),
        )
        return user
