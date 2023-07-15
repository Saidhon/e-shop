from django.db import models

# Create your models here.
class Mobile_type(models.Model):
    nomi =models.CharField(max_length=20)
    def __str__(self):
        return self.nomi

class Mobile_maxsulot(models.Model):
    nomi = models.CharField(max_length=30)
    old_narx = models.IntegerField()
    new_narx = models.IntegerField()
    type = models.ForeignKey(Mobile_type,on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')

class AccesType(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi

class SuvenirProduct(models.Model):
    nomi = models.CharField(max_length=30)
    narxi = models.CharField(max_length=30)
    rasm = models.ImageField(upload_to='media')


class TopProduct(models.Model):
    nomi = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    new_narx = models.CharField(max_length=30)
    old_narx = models.CharField(max_length=30)
    rasm = models.ImageField(upload_to='media')

class SpecialProduct(models.Model):
    nomi = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    new_narx = models.CharField(max_length=30)
    old_narx = models.CharField(max_length=30)
    rasm = models.ImageField(upload_to='media')

class AccesMaxulotlar(models.Model):
    nomi = models.CharField(max_length=40)
    price = models.IntegerField()
    tur = models.ForeignKey(AccesType,on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')
    # sizga_yoqadi = models.BooleanField(default=False)
    # sotildi = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nomi
    
class SizgaYoqishiMumkin(models.Model):
    turi = models.CharField(max_length=90)
    nomi = models.CharField(max_length=40)
    price = models.IntegerField()
    rasm = models.ImageField(upload_to='media')

class Card(models.Model):
    nomi = models.CharField(max_length=50)
    narx = models.IntegerField()
    soni = models.IntegerField(default=1)
    tur = models.TimeField(auto_now=True)
    vaqt = models.DateTimeField(auto_now=True)



# ------------------------------FILTER-----------------------------------------

class Notebooks(models.Model):

    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

# class Printers(models.Model):
#     nomi = models.CharField(max_length=30)
#     def __str__(self):
#         return self.nomi

# class Keys(models.Model):
#     nomi = models.CharField(max_length=30)
#     def __str__(self):
#         return self.nomi


# class Aksessuar(models.Model):
#     nomi = models.CharField(max_length=30)
#     def __str__(self):
#         return self.nomi


# class GameDevice(models.Model):
#     nomi = models.CharField(max_length=30)
#     def __str__(self):
#         return self.nomi




