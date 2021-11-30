from django.contrib import admin
from .models  import EnquiryData
# Register your models here.


class EnquiryDataAdmin(admin.ModelAdmin):

    list_display = ('name','email','mobile')


# admin.site.register(EnquiryData,EnquiryDataAdmin)
admin.site.register(EnquiryData, EnquiryDataAdmin)
