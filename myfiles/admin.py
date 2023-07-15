from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminMobile_type(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Mobile_type,AdminMobile_type)


class AdminMobile_maxsulot(admin.ModelAdmin):
    list_display = ['id','nomi','old_narx','new_narx','type','rasm']
admin.site.register(Mobile_maxsulot,AdminMobile_maxsulot)


class AdminAccesType(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(AccesType,AdminAccesType)


class AdminAccesMaxulotlar(admin.ModelAdmin):
    list_display = ['id','nomi','price','tur','rasm']
admin.site.register(AccesMaxulotlar,AdminAccesMaxulotlar)




class AdminCard(admin.ModelAdmin):
    list_display = ['id','nomi','narx','soni','tur','vaqt']
admin.site.register(Card,AdminCard)


class AdminSuvenirProduct(admin.ModelAdmin):
    list_display = ['id','nomi','narxi','rasm']
admin.site.register(SuvenirProduct,AdminSuvenirProduct)


class AdminTopProduct(admin.ModelAdmin):
    list_display = ['id','nomi','type','new_narx','old_narx','rasm']
admin.site.register(TopProduct,AdminTopProduct)


class AdminSpecialProduct(admin.ModelAdmin):
    list_display = ['id','nomi','type','new_narx','old_narx','rasm']
admin.site.register(SpecialProduct,AdminSpecialProduct)


class AdminSizgaYoqishiMumkin(admin.ModelAdmin):
    list_display = ["id","turi","nomi","price","rasm"]
admin.site.register(SizgaYoqishiMumkin,AdminSizgaYoqishiMumkin)



# ----------------------------------------FILTER-------------------------



class AdminNotebooks(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Notebooks,AdminNotebooks)

# class AdminPrinters(admin.ModelAdmin):
#     list_display = ['id','nomi']
# admin.site.register(Printers,AdminPrinters)

# class AdminKeys(admin.ModelAdmin):
#     list_display = ['id','nomi']
# admin.site.register(Keys,AdminKeys)

# class AdminAksessuar(admin.ModelAdmin):
#     list_display = ['id','nomi']
# admin.site.register(Aksessuar,AdminAksessuar)

# class AdminGameDevice(admin.ModelAdmin):
#     list_display = ['id','nomi']
# admin.site.register(GameDevice,AdminGameDevice)



