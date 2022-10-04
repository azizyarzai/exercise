
from enum import unique
from sre_constants import MAX_UNTIL
from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify
from products.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

CATEGORIES = [
    ("el", 'Electronics'),
    ("gr", 'Groceries')
]


def check_price(val):
    if val > 0:
        return val
    raise ValidationError("Please enter a positive.")


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=500, unique=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[check_price])
    category = models.CharField(max_length=20, choices=CATEGORIES)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products-imgs', null=True, blank=True)
    description = models.TextField(
        null=True, blank=True, default="This is a product")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self):
        # self.price = float(self.price) + 10
        # self.slug = unique_slug_generator(self)
        super().save()

    def __str__(self) -> str:
        return f"{self.name} - {self.pk}"

    class Meta:
        db_table = 'product'
        ordering = ['price']


class Test(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        managed = True


def pres_save_product(sender, instance, *args, **kwargs):
    instance.slug = unique_slug_generator(instance)
    print("pre_save called.")


pre_save.connect(pres_save_product, sender=Product)


def post_save_product(sender, instance, created, *args, **kwargs):
    if created:
        print("post save called")
        instance.price = float(instance.price) + 100
        instance.save()


post_save.connect(post_save_product, sender=Product)
