from django.contrib import admin
from homeapp.models import standard,ecommlite,ecommpro
# Register your models here.

class dis(admin.ModelAdmin):
    list_display=['uid','firstname','lastname','email','mobnumber','plan','message']

admin.site.register(standard,dis)
admin.site.register(ecommlite,dis)
admin.site.register(ecommpro,dis)