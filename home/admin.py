from django.contrib import admin
from .models import *


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created','updated')
    list_filter = ('name','created','updated',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','amount','available','unitPrice','discount','totalPrice')
    list_filter = ('category','available','discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

