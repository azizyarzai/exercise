from operator import truediv
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(unique=True, max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)
    



class Test(models.Model):
    test1 = models.CharField(max_length=250)
    test2 = models.IntegerField()