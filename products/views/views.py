from products.serializers import Test
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView
from products.forms import ProductModelForm, TestForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import View, TemplateView
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework.views import APIView


from django.db.models import Q

from products.models import Product


# Create your views here.

# list product
def list_products(request):
    # products = Product.objects.filter(
    #     Q(is_available=True) | Q(category='el'), price=13100)  # SELECT * FROM products.s
    # print(products.query)

    products = Product.objects.get_availibes()
    # for p in products:
    #     print(p.get_price)
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
        image = request.FILES.get('image')

        product = Product.objects.create(
            name=name, price=price,
            is_available=bool(is_available),
            category=category,
            description=desc,
            image=image
        )
        messages.success(request, 'Product created succesfully.')
        # product.price = float(product.price) +  100
        # product.save()

        return redirect(reverse_lazy('products:list'))


# update product
def update_product(request, prod_slug):
    if request.method == 'GET':
        product = Product.objects.get(slug=prod_slug)
        return render(request, 'products/update-product.html', {'product': product})
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        is_available = request.POST.get('is_available')
        category = request.POST.get('category')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')

        product = Product.objects.get(slug=prod_slug)

        product.name = name
        product.price = price
        product.is_available = bool(is_available)
        product.category = category
        product.description = desc

        if image:
            if os.path.exists(product.image.path):
                os.remove(product.image.path)
            product.image = image

        product.save()

        return redirect(reverse_lazy('products:update', args=[prod_slug]))
        # return HttpResponse(f"Update id - {product.id} - {product.created}")

# delete product


def delete_product(request, prod_slug):
    product = Product.objects.get(slug=prod_slug)

    if os.path.exists(product.image.path):
        os.remove(product.image.path)

    product.delete()

    return HttpResponse(f"Deleted {prod_slug}")


@login_required
def show_news(request):
    print("request", request.path)
    return HttpResponse("Welcome to Django")


@login_required
def home(request):
    if request.method == 'GET':
        # form = TestForm(initial={'age': 12, 'name': 'karim'})
        form = TestForm()
        return render(request, 'index.html', {"title": "Hello World 2", "name": "Ahmad", 'form': form})
    else:
        # request.POST.update(image=request.FILES.get('image'))
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)

            return HttpResponse("Submited")
        print(form.errors)
        return render(request, 'index.html', {"title": "Hello World 2", "name": "Ahmad", 'form': form})

    # if request.method == 'GET':
    #     form = ProductModelForm()
    #     return render(request, 'index.html', {"title": "Hello World 2", "name": "Ahmad", 'form': form})
    # else:
    #     # request.POST.update(image=request.FILES.get('image'))
    #     form = ProductModelForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()

    #         return redirect(reverse_lazy('products:list'))
    #     print(form.errors)
    #     return render(request, 'index.html', {"title": "Hello World 2", "name": "Ahmad", 'form': form})


def product_detail(request, prod_slug):
    try:
        product = Product.objects.get(slug=prod_slug)
    except Product.DoesNotExist:
        raise Http404()
    except Product.MultipleObjectsReturned:
        return render(request, 'index.html')

    # product = get_object_or_404(Product, slug=prod_slug)
    return render(request, 'products/product-detail.html', {'product': product})


# class ListProduct(View):
#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all()

#         return render(request, 'products/list-products.html', {'products': products})
class ListProduct(TemplateView):
    # template_name = 'about.html'

    # def get_template_names(self):

    #     return ['about.html']

    pass


class ProductListView(ListView):
    # model = Product
    queryset = Product.objects.get_availibes()
    template_name = 'products/list-products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'list View'
        context['no'] = 50
        context['today'] = datetime.now()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    # slug_field = 'id'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'is_available',
              'description', 'image', 'category']
    template_name = 'products/create-class.html'
    success_url = reverse_lazy("products:list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'is_available',
              'description', 'image', 'category']
    template_name = 'products/update-class.html'
    success_url = reverse_lazy("products:list")


# def test(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         return JsonResponse(data, safe=False)

#     return JsonResponse([{"name": "product 1", "price": 1400}, {"name": "product 2", "price": 1500}], safe=False)


@api_view(['GET', 'POST'])
def test(request):
    # print(request.data[0]['age'])
    return Response([{"name": "product 1", "price": 20000}, {"name": "product 2", "price": 1500}])


class ProductAPIView(APIView):
    def get(self, request, *arg, **kwaargs):
        return Response([{"name": "product 1", "price": 20000}, {"name": "product 2", "price": 1500}])

    def post(self, request, *arg, **kwaargs):
        res = Test(data=request.data)
        data1 = {
            "name": 'jdsfhskdjfhsksdfj',
            'price': 12
        }
        if res.is_valid():
            res2 = Test(data1)
            print(res2.is_valid())
            return Response(res2.data)
        else:
            return Response(res.errors)
