from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "old_price",
        "badge",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "badge",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    list_editable = (
        "price",
        "old_price",
        "is_active",
    )

    ordering = ("-created_at",)