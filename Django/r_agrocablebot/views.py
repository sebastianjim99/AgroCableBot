from rest_framework import viewsets, generics, permissions

from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

import json
from django.http import JsonResponse
from r_agrocablebot.mqtt import client as mqtt_client
from django.views.decorators.csrf import csrf_exempt
import paho.mqtt.publish as publish
import os 

from .models import (
    acciones,
    tipoSensor,
    tipoCultivo,
    sensor,
    cultivo,
    plantas,
    imagenesxPlanta,
    calendarios,
    Mensaje,
    Sensor_MQTT,
    eventosCalendarios
)

from .serializers import (
    MensajeSerializer,
    accionesSerializer,
    tipoSensorSerializer,
    tipoCultivoSerializer,
    sensorSerializer,
    cultivoSerializer,
    plantasSerializer,
    imagenesxPlantaSerializer,
    calendariosSerializer,
    Sensor_MQTTSerializer,
    eventosCalendariosSerializer

)

# Create your views here.
class accionesViewSet(viewsets.ModelViewSet):
    queryset = acciones.objects.all()
    serializer_class = accionesSerializer

class tiposensorViewSet(viewsets.ModelViewSet):
    queryset = tipoSensor.objects.all()
    serializer_class = tipoSensorSerializer
class tipoCultivoViewSet(viewsets.ModelViewSet):
    queryset = tipoCultivo.objects.all()
    serializer_class = tipoCultivoSerializer

class sensorViewSet(viewsets.ModelViewSet):
    queryset = sensor.objects.all()
    serializer_class = sensorSerializer

class cultivoViewSet(viewsets.ModelViewSet):
    queryset = cultivo.objects.all()
    serializer_class =cultivoSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Verificar si se debe eliminar los sensores asociados al cultivo
        if 'sensores' in request.data and request.data['sensores'] == 'eliminar_sensores':
            instance.sensores.clear()  # Eliminar todos los sensores asociados

        self.perform_update(serializer)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class plantasViewSet(viewsets.ModelViewSet):
    queryset = plantas.objects.all()
    serializer_class =plantasSerializer

class imagenesxPlantaViewSet(viewsets.ModelViewSet):
    queryset = imagenesxPlanta.objects.all()
    serializer_class =imagenesxPlantaSerializer

class calendariosViewSet(viewsets.ModelViewSet):
    queryset = calendarios.objects.all()
    serializer_class =calendariosSerializer
    
@csrf_exempt
def publish_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': rc})

@csrf_exempt
def enviar_mensaje_mqtt(request):
    if request.method == 'POST':
        message = {
            'interface': 'send_aio'
        }
        try:
            # Definir las credenciales del cliente MQTT
            auth = {
                'username': 'imacuna',
                'password': 'pi'
            }

            # Publicar el mensaje MQTT con cliente y contraseña especificados
            publish.single('comandos', json.dumps(message), hostname=os.environ['MQTT_SERVER'], auth=auth)
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})  





class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer


class Sensor_MQTTViewSet(viewsets.ModelViewSet):
    queryset = Sensor_MQTT.objects.all()
    serializer_class = Sensor_MQTTSerializer


class eventosCalendariosViewSet(viewsets.ModelViewSet):
    queryset = eventosCalendarios.objects.all()
    serializer_class = eventosCalendariosSerializer
    
