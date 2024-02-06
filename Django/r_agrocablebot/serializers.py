from rest_framework import serializers
from .models import *


class accionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = acciones
        fields = '__all__'

class tipoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoSensor
        fields = '__all__'

class tipoCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoCultivo
        fields = '__all__'

class cultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = cultivo
        fields = '__all__'

class plantasSerializer(serializers.ModelSerializer):

    cultivo=cultivoSerializer(read_only=True)

    class Meta:
        model = plantas
        fields = '__all__'

class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensor
        fields = '__all__'

class imagenesxPlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = imagenesxPlanta
        fields = '__all__'

# class tablasEstadisticasSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = tablasEstadisticas
#         fields = '__all__'

# class graficosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = graficos
#         fields = '__all__'

# class estadisticasSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = estadisticas
#         fields = '__all__'

class calendariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = calendarios
        fields = '__all__'

# class mo_agroCableBotSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = mo_agroCableBot
#         fields = '__all__'