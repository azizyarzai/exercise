from rest_framework import serializers
from products.models import Product

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'role']


class Test(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    price = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Product
        exclude = ['slug']


class UserField(serializers.RelatedField):
    def to_native(self, value):
        return {str(value.pk): value.name}


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'user', 'price',
                  'category', 'is_available', 'description']
