from django.db import models

# Create your models here.

class Cartas(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.FloatField()
    # imagen
    stock = models.IntegerField()

class Comprador(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)

class Vendedor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)