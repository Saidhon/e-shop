from django.shortcuts import render
from myfiles.models import *
from django.urls import reverse

def index(malumot):
    maxsulot = AccesMaxulotlar.objects.all()
    maxsulot2 = SuvenirProduct.objects.all()
    maxsulot3 = TopProduct.objects.all()
    maxsulot4 = SizgaYoqishiMumkin.objects.all()
    cart = Card.objects.all()

    # printer = Printers.objects.all()
    # keys = Keys.objects.all()
    # aksessuar = Aksessuar.objects.all()
    # gamedevice = GameDevice.objects.all()
    context = {
        "maxsulot": maxsulot,
        "maxsulot2": maxsulot2,
        "maxsulot3":maxsulot3,
        "maxsulot4":maxsulot4,
        "korzinka":cart,
        # "printer": printer,
        # "keys": keys,
        # "aksessuar": aksessuar,
        # "gamedevice": gamedevice,
    }
    return render(malumot,'index.html', context)

def index_filter(malumot,id):
    notebook = AccesMaxulotlar.objects.filter(id=id)
    print("------------------")
    print(notebook)
    print("------------------")
    return render(malumot,'shop_full.html',{'maxsulot': notebook})




def full_shop(malumot):
    maxsulot = AccesMaxulotlar.objects.all()

    # notebook = Notebooks.objects.all()
    # printer = Printers.objects.all()
    # keys = Keys.objects.all()
    # aksessuar = Aksessuar.objects.all()
    # gamedevice = GameDevice.objects.all()
    context = {
        "maxsulot": maxsulot,

        # "notebook": notebook,
        # "printer": printer,
        # "keys": keys,
        # "aksessuar": aksessuar,
        # "gamedevice": gamedevice,
    }
    return render(malumot,'shop_full.html',context)

def onsale(malumot, pr_id=None):
    maxsulot = AccesMaxulotlar.objects.filter(id=pr_id)
    maxsulot4 = SizgaYoqishiMumkin.objects.filter(id=pr_id)
    if not maxsulot.exists():
        return render(reverse("index"))
    else:
        maxsulot = maxsulot.first()
    context  = {
        "product":maxsulot,
        "maxsulot4":maxsulot4,
        "products":AccesMaxulotlar.objects.all()
    }
    return render(malumot,'onsale.html', context)


def onsale2(malumot, pr_id=None):
    maxsulot4 = SizgaYoqishiMumkin.objects.filter(id=pr_id)
    if not maxsulot4.exists():
        return render(reverse("index"))
    else:
        maxsulot4 = maxsulot4.first()
    context  = {
        "product":maxsulot4,
        "products":AccesMaxulotlar.objects.all()
    }
    return render(malumot,'onsale.html', context)


def onsale3(malumot, pr_id=None):
    maxsulot2 = SuvenirProduct.objects.filter(id=pr_id)
    if not maxsulot2.exists():
        return render(reverse("index"))
    else:
        maxsulot2 = maxsulot2.first()
    context  = {
        "product":maxsulot2,
        "products":AccesMaxulotlar.objects.all()
    }
    return render(malumot,'onsale.html', context)


def checkout(malumot):
    maxsulot2 = SuvenirProduct.objects.all()
    context = {
        "maxsulot2": maxsulot2,
    }
    return render(malumot,'checkout.html',context)

def cart(malumot):
    return render(malumot,'cart.html')