
from django.db import models
from django.forms import ValidationError

CATEGORIES = [
    ("el", 'Electronics'),
    ("gr", 'Groceries')
]


def check_price(val):
    if val > 0:
        return val
    raise ValidationError("Please enter a positive.")


class Product(models.Model):
    name = models.CharField(unique=True, max_length=150)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[check_price])
    category = models.CharField(max_length=20, choices=CATEGORIES)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products-imgs', null=True, blank=True)
    description = models.TextField(
        null=True, blank=True, default="This is a product")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.pk}"
