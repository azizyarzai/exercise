from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from products.models import Product


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


# update product
def update_product(request, prod_id):
    pass

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

