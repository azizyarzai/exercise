from math import prod
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from products.models import Product

import decimal


# Create your views here.

# list product
def list_products(request):
    products = Product.objects.all()  # SELECT * FROM products.
    # print(products)
    # for product in products:
    #     print(product.name, product.price)

    return render(request, 'products/list-products.html', {'products': products})


# Create product
def create_product(request):
    if request.method == "GET":
        return render(request, 'products/create-product.html')
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        is_available = request.POST.get('is_available')
        category = request.POST.get('category')
        desc = request.POST.get('desc')

        product = Product.objects.create(
            name=name, price=price,
            is_available=bool(is_available), 
            category=category,
            description=desc
        )

        product.price = float(product.price) +  100
        product.save()


        return HttpResponse(f"Created id - {product.id} - {product.created}")


# update product
def update_product(request, prod_id):
    if request.method == 'GET':
        product = Product.objects.get(id=prod_id)
        return render(request, 'products/update-product.html', {'product': product})

# delete product
def delete_product(request, prod_id):
    pass





@login_required
def show_news(request):
    print("request", request.path)
    return HttpResponse("Welcome to Django")

@login_required
def home(request):
    
    #print("request", dir(request))
    #print(request.path)

    # if request.user.is_authenticated:
    return render(request, 'index.html',{"title": "Hello World 2", "name": "Ahmad"})
    # else:
    #     return HttpResponse("Please Login to access this page.")

