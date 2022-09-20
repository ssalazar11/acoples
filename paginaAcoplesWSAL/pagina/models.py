from django.db import models

# Create your models here.

class producto(models.Model):
    codigo=models.CharField(max_length=20, primary_key=True)
    tipo=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=100)
    unidad=models.CharField(max_length=20)
    valorUnidad=models.IntegerField()
