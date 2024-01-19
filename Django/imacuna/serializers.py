from rest_framework import serializers
from .models import Lineas_investigacion, Servicios, Usuarios, facultades, programa,tipoIntegrante, integrante, proyectos, imagenesProyectos, videoProyectos 


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

class facultadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = facultades
        fields = '__all__'

class programaSerializer(serializers.ModelSerializer):
    class Meta:
        model = programa
        fields = '__all__'
class tipoIntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoIntegrante
        fields = '__all__'

class integranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = integrante
        fields = '__all__'
class proyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = proyectos
        fields = '__all__'

class imagenesProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = imagenesProyectos
        fields = '__all__'
class videoProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = videoProyectos
        fields = '__all__'
