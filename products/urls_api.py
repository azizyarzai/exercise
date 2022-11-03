
from django.urls import path
from products.views.api import product_list


app_name = 'products-api'

urlpatterns = [
    path("", product_list)

]
