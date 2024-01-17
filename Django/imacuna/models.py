from django.db import models
from django.conf import settings 
from rest_framework import generics
#lINEAS DE INVESTIGACIÓN

class Lineas_investigacion(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100 , verbose_name="Nombre", null=True)
    imagen = models.ImageField(upload_to='iconos/', verbose_name="imagen", null= True )


class Servicios(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100 , verbose_name="Nombre", null=True)
    imagen = models.ImageField(upload_to='iconos/', verbose_name="imagen", null= True )
    

#roles - Estudiantes, Profesores, operarios
class Roles(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 50 , verbose_name="rol" )


# Usuario de otra forma
class Usuarios(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , related_name= 'usuarios', on_delete= models.CASCADE)
    nombre = models.CharField(max_length=150)
    Completado = models.BooleanField(default=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.nombre


