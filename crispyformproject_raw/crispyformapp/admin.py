from django.contrib import admin

from .models import Course,Collage,Location,Branch,Institute

admin.site.register(Collage)
admin.site.register(Course)
admin.site.register(Location)
admin.site.register(Branch)
admin.site.register(Institute)
