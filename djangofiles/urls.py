"""djangofiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from djangofiles import settings
from django.contrib import admin
from django.urls import path, include
from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('full_shop',Homeview,name='full_shop'),
    path('indx_filter/notebook/<str:id>/',Homeview,name='indx_filter'),
    path('onsale/',onsale,name='onsale'),
    path('onsale/like/',onsale,name='onsale2'),
    path('onsale/suvenir/',onsale,name='onsale3'),
    path('checkout',Homeview,name='checkout'),
    path('cart/',Homeview,name='cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIAFILE_DIRS)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)