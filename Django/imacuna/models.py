from django.db import models

# Create your models here.

class Lineas_investigacion(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100 , verbose_name="Nombre", null=True)
    imagen = models.ImageField(upload_to='iconos/', verbose_name="imagen", null= True )
    

class Servicios(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100 , verbose_name="Nombre", null=True)
    imagen = models.ImageField(upload_to='iconos/', verbose_name="imagen", null= True )
    