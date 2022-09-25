from math import prod
from django.shortcuts import render, redirect
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


        return redirect('/products/')


# update product
def update_product(request, prod_id):
    if request.method == 'GET':
        product = Product.objects.get(id=prod_id)
        return render(request, 'products/update-product.html', {'product': product})
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        is_available = request.POST.get('is_available')
        category = request.POST.get('category')
        desc = request.POST.get('desc')

        # product = Product.objects.get(id=prod_id)

        # product.name = name
        # product.price = price
        # product.is_available = bool(is_available)
        # product.category = category
        # product.description = desc

        products = Product.objects.filter(id=prod_id)
        products.update(name = name, price=price, is_available=bool(is_available), category= category, description= desc)

        # products.save()


        return HttpResponse(f"Update id - {products[0].id} - {products[0].created}")
        # return HttpResponse(f"Update id - {product.id} - {product.created}")

# delete product
def delete_product(request, prod_id):
    product = Product.objects.get(id= prod_id)

    pro_id = product.id
    product.delete()

    return HttpResponse(f"Deleted {pro_id}")





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

