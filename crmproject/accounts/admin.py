from django.contrib import admin
from .models import Customers, Products,Orders

class Admincustomer(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'created_date']
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'Category', 'Description', 'created_date']
class AdminOrders(admin.ModelAdmin):
    list_display = ['customer','product','status','created_date']


admin.site.register(Customers, Admincustomer)
admin.site.register(Products, AdminProduct)
admin.site.register(Orders, AdminOrders)

