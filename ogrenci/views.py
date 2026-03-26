from rest_framework import viewsets
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Ogrenci
from .serializers import OgrenciSerializer

# 1. API GÖRÜNÜMLERİ (Flutter İçin)
class OgrenciViewSet(viewsets.ModelViewSet):
    queryset = Ogrenci.objects.all()
    serializer_class = OgrenciSerializer

# 2. WEB ARAYÜZÜ GÖRÜNÜMLERİ (Tarayıcı İçin)
class OgrenciListView(ListView):
    model = Ogrenci
    template_name = 'ogrenci/liste.html'
    context_object_name = 'ogrenciler'

class OgrenciCreateView(CreateView):
    model = Ogrenci
    fields = ['ad', 'soyad', 'numara']
    template_name = 'ogrenci/form.html'
    success_url = reverse_lazy('ogrenci_liste')

class OgrenciUpdateView(UpdateView):
    model = Ogrenci
    fields = ['ad', 'soyad', 'numara']
    template_name = 'ogrenci/form.html'
    success_url = reverse_lazy('ogrenci_liste')

class OgrenciDeleteView(DeleteView):
    model = Ogrenci
    template_name = 'ogrenci/sil_onay.html'
    success_url = reverse_lazy('ogrenci_liste')