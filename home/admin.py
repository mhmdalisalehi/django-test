from django.contrib import admin
from .models import *


class ProductVariantsInline(admin.TabularInline):
    model = Variants


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created','updated')
    list_filter = ('name','created','updated',)
    prepopulated_fields = {'slug':('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','amount','available','unitPrice','discount','totalPrice')
    list_filter = ('category','available','discount')
    prepopulated_fields = {'slug':('name',)}
    inlines = [ProductVariantsInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Variants)
admin.site.register(Size)
admin.site.register(Color)


