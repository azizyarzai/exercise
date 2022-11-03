from rest_framework import serializers
from products.models import Product


class Test(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    price = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['slug']


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id', 'slug', 'created', 'updated']
