from django.contrib import admin
from.models import *
# Register your models here.

class catgadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(Categ,catgadmin)

class prodAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img','available']
    list_editable=['price','stock','img','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Products,prodAdmin)
admin.site.register(CartList)
admin.site.register(CartItem)


