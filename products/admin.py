from django.contrib import admin
from products.models import *
# Register your models here.


class ProductTypeModel(admin.ModelAdmin):
    list_display = ['id', 'name']
    
admin.site.register(ProductType,ProductTypeModel)


class ProductBrendModel(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(ProductBrend,ProductBrendModel)


class ProductsAdminModel(admin.ModelAdmin):
    list_display = ['name', 'brend', 'type', 'amount', 'sell_price']
    exclude = ('top_reyting',)
admin.site.register(Products,ProductsAdminModel)
