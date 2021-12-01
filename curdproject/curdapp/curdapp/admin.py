from django.contrib import admin
from .models import ProductsData

# Register your models here.

# admin.site.register(ProductsData)

class ProductAdmin(admin.ModelAdmin):

    list_display = ('product_id', 'product_name', 'product_class','product_price','customer_name','mobile','email')


admin.site.register(ProductsData,ProductAdmin)