"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ogrenci.views import (
    OgrenciViewSet, 
    OgrenciListView, OgrenciCreateView, OgrenciUpdateView, OgrenciDeleteView
)

# API Rotaları
router = DefaultRouter()
router.register(r'ogrenciler', OgrenciViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Flutter buraya bağlanacak
    
    # Web Arayüzü Rotaları
    path('', OgrenciListView.as_view(), name='ogrenci_liste'),
    path('ekle/', OgrenciCreateView.as_view(), name='ogrenci_ekle'),
    path('guncelle/<int:pk>/', OgrenciUpdateView.as_view(), name='ogrenci_guncelle'),
    path('sil/<int:pk>/', OgrenciDeleteView.as_view(), name='ogrenci_sil'),
]