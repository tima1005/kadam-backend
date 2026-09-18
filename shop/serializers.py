from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    image = serializers.ImageField(
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "category_name",
            "price",
            "old_price",
            "image",
            "badge",
            "description",
            "is_active",
        ]