from django.db import models

# Create your models here.
class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, verbose_name='Nombre')
    pais = models.CharField(max_length=50, null=True, verbose_name='Pais')
    estrellas = models.FloatField(null=True, verbose_name='Numero de estrellas')
    escudo = models.ImageField(upload_to='img/', null=True, verbose_name='Imagen del escudo')
