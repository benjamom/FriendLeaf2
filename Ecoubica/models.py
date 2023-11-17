from django.db import models
from django.contrib.auth.models import AbstractUser

class location(models.Model):
    name = models.CharField(max_length=250, verbose_name = 'Punto Verde')
    adress = models.CharField(max_length=250, verbose_name='Direccion')
    state = models.CharField(max_length=250, verbose_name='Estado')
    lat = models.FloatField(verbose_name='Latitud')
    lng = models.FloatField(verbose_name='Longitud')

    class Meta:
        verbose_name = 'Punto Verde'
        verbose_name_plural='Puntos Verdes'
        ordering = ['name']

    def __str__(self):
        return self.name    

