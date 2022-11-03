

from rest_framework.decorators import api_view
from products.models import Product
from rest_framework.response import Response
from products.serializers import ProductSerializer, ProductCreateSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        ser = ProductSerializer(products, many=True)
        return Response(ser.data)
    elif request.method == "POST":
        res = ProductCreateSerializer(data=request.data)
        if res.is_valid():
            return Response(res.validated_data)
        else:
            return Response(res.errors)
