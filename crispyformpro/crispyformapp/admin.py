from django.contrib import admin
from .models import College,Course,Branch,Location
# Register your models here

admin.site.register(College)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Location)