
from django.urls import path
from products.views import (
    ProductDetailView,
    list_products,
    create_product,
    delete_product,
    update_product,
    product_detail,
    ListProduct,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView
)

from django.views.generic.base import View, TemplateView


app_name = 'products'

urlpatterns = [
    # path("", TemplateView.as_view(template_name='about.html'), name='list'),
    path("", ProductListView.as_view(), name='list'),
    path("create/", create_product, name='create'),
    path("delete/<slug:prod_slug>/", delete_product, name="delete"),
    path("update/<slug:slug>/", ProductUpdateView.as_view(), name='update'),
    path("<slug:prod_slug>/", product_detail, name='detail'),

]
