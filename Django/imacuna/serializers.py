from dataclasses import fields
from rest_framework import serializers
from .models import Lineas_investigacion, Servicios


class Lineas_investigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lineas_investigacion
        fields = ['id', 'nombre', 'imagen']

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ['id', 'nombre', 'imagen']
