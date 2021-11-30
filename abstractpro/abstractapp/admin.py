from django.contrib import admin
from .models import  Customer, Student, Emp


# Register your models here.

class AdminEmp(admin.ModelAdmin):
    list_display = ['name', 'location', 'email','sal']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['name', 'location','email','sales']


class AdminStudent(admin.ModelAdmin):
    list_display = ['name', 'location', 'email','marks']


admin.site.register(Emp, AdminEmp)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Student, AdminStudent)
