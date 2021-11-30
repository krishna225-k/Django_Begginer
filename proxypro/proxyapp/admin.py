from django.contrib import admin
from .models import Student, StudentProxy


# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display = ['name', 'email', 'location', 'marks']


class AdminStudentProxy(admin.ModelAdmin):
    list_display = ['name', 'email', 'location', 'marks']


admin.site.register(Student,AdminStudent)
admin.site.register(StudentProxy,AdminStudentProxy)

