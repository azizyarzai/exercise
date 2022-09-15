from django.contrib import admin
from products.models import Product

# Register your models here.



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' ,'category', 'price', 'is_available']
    list_display_links= ['name']
    list_editable = ['is_available', 'price']
    list_filter = ['is_available', 'created']
    list_per_page = 25
    ordering= ['-price']
    search_fields= ['name', 'price']

# admin.site.register(Product, ProductAdmin)
