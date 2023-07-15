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
from django.urls import path
from myfiles.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('full_shop',full_shop,name='full_shop'),
    path('indx_filter/notebook/<str:id>/',index_filter,name='indx_filter'),
    path('onsale/<str:pr_id>/',onsale,name='onsale'),
    path('onsale/like/<str:pr_id>/',onsale2,name='onsale2'),
    path('onsale/suvenir/<str:pr_id>/',onsale3,name='onsale3'),
    path('checkout',checkout,name='checkout'),
    path('cart/',cart,name='cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIAFILE_DIRS)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)