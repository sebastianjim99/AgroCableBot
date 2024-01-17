from rest_framework import serializers
from .models import Lineas_investigacion, Servicios, Usuarios


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['user', 'nombre', 'Completado', 'fecha_creado', 'fecha_actualizado']


class Lineas_investigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lineas_investigacion
        fields = ['id', 'nombre', 'imagen']

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ['id', 'nombre', 'imagen']
