from django.contrib import admin
from .models import Emp, Customer, Student, Book


# Register your models here.

class AdminEmp(admin.ModelAdmin):
    list_display = ['ename', 'sal']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname', 'sales']


class AdminStudent(admin.ModelAdmin):
    list_display = ['sname', 'marks']


class AdminBook(admin.ModelAdmin):
    list_display = ['bname', 'cost']


admin.site.register(Emp, AdminEmp)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Student, AdminStudent)
admin.site.register(Book, AdminBook)


class AdminBook(admin.ModelAdmin):
    list_display = ['bname', 'cost']
