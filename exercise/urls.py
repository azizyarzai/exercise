"""exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from products.views.views import show_news, home

from django.conf import settings
from django.conf.urls.static import static
from products.views.views import test, ProductAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/", include("products.urls")),
    path("api/products/", include("products.urls_api")),
    path("accounts/", include("accounts.urls")),
    path('news/hi/', show_news),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("api/products/", ProductAPIView.as_view()),
    path("", home, name="home")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Test"
