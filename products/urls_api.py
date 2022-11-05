
from django.urls import path, include
from products.views.api import product_list, ProductListView, ProductCreateView, ProdcutViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", ProdcutViewSet)

app_name = 'products-api'


urlpatterns = [
    path("", ProductListView.as_view()),
    path("create/", ProductCreateView.as_view()),
    path("viewset/", include(router.urls))

]
