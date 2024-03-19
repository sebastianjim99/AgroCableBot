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
    # tipoCultivo=tipoCultivoSerializer()
    tipoCultivo=serializers.PrimaryKeyRelatedField(queryset=tipoCultivo.objects.all())
    sensores = serializers.PrimaryKeyRelatedField(queryset=sensor.objects.all(), required=False, many=True)
    class Meta:
        model = cultivo
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tipo_cultivo_data = tipoCultivoSerializer(instance.tipoCultivo).data
        representation['tipoCultivo'] = tipo_cultivo_data
        return representation

    

    

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
    plantas = serializers.PrimaryKeyRelatedField(queryset=plantas.objects.all(), required=False, many=True)
    cultivo = serializers.PrimaryKeyRelatedField(queryset=cultivo.objects.all(), required=False, many=True)
    # repeticion=serializers.ReadOnlyField(source='get_repeticion_display')
    class Meta:
        model = calendarios
        fields = '__all__'

# class mo_agroCableBotSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = mo_agroCableBot
#         fields = '__all__'


class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'

class Sensor_MQTTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor_MQTT
        fields = '__all__'
        
class eventosCalendariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = eventosCalendarios
        fields = '__all__'
