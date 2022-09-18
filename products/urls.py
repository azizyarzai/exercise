
from django.urls import path
from products.views import list_products, create_product, delete_product, update_product


urlpatterns = [
    path("", list_products),
    path("create/", create_product),
    path("delete/<int:prod_id>/", delete_product),
    path("update/<int:prod_id>/", update_product),

]
