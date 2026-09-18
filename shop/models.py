from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    BADGE_CHOICES = [
        ("", "Без значка"),
        ("NEW", "NEW"),
        ("SALE", "SALE"),
    ]

    name = models.CharField("Название", max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория"
    )

    price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2
    )

    old_price = models.DecimalField(
        "Старая цена",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    image = models.ImageField(
        "Фото",
        upload_to="products/"
    )

    badge = models.CharField(
        "Значок",
        max_length=20,
        choices=BADGE_CHOICES,
        blank=True,
        default=""
    )

    description = models.TextField(
        "Описание",
        blank=True
    )

    is_active = models.BooleanField(
        "Показывать на сайте",
        default=True
    )

    created_at = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name