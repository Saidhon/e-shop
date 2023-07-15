from django.db import models


class ProductType(models.Model):
    name = models.CharField(verbose_name="Maxsulot turi", max_length=30)


class ProductBrend(models.Model):
    name = models.CharField(verbose_name="Brend nomi", max_length=30)

class Products(models.Model):
    name = models.CharField(verbose_name="maxsulot nomi", max_length=40)
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    brend = models.ForeignKey(ProductBrend, on_delete=models.SET_NULL, null=True) # maxsulot brend misol uchun [lenovo, acer, samsung]
    image = models.ImageField(verbose_name="Maxsulot rasmi", upload_to='media')
    top_reyting = models.IntegerField(default=0) # Maxsulot top reytingi 
    input_price = models.FloatField(verbose_name="kirim narxi") # kirim narxi
    sell_price = models.FloatField(verbose_name="sotuv narxi") # sotilish narxi
    amount = models.IntegerField(verbose_name="maxsulot miqdori", default=0)
    discount = models.IntegerField(verbose_name="maxsulot chegirmasi", default=0)


