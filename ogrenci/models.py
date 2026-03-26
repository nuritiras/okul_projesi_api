from django.db import models

class Ogrenci(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    numara = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"