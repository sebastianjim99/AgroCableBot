from rest_framework import viewsets, generics, permissions

from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

import json
from django.http import JsonResponse
# from r_agrocablebot.mqtt import client as mqtt_client
from django.views.decorators.csrf import csrf_exempt
import paho.mqtt.publish as publish
from django.http import HttpResponse
import os 

#Empaquetado de datos
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import csv

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
    eventosCalendarios,
    RutinaCodigoG,
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
    eventosCalendariosSerializer,
    RutinaCodigoGSerializer,

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


# @csrf_exempt
# def publish_message(request):
#     message = {
#             'interface': 'send_aio'
#         }
#     # Definir las credenciales del cliente MQTT
#     auth = {
#         'username': 'imacuna',
#         'password': 'pi'
#     }
#     publish.single("comandos", json.dumps(message), hostname=os.environ['MQTT_SERVER'], auth=auth)
#     return HttpResponse("Published")

# @csrf_exempt
# def enviar_mensaje_mqtt(request):
#     if request.method == 'POST':
#         message = {
#             'interface': 'send_aio'
#         }
#         try:
#             # Definir las credenciales del cliente MQTT
#             auth = {
#                 'username': 'imacuna',
#                 'password': 'pi'
#             }

#             # Publicar el mensaje MQTT con cliente y contraseña especificados
#             publish.single('comandos', json.dumps(message), hostname=os.environ['MQTT_SERVER'], auth=auth)
            
#             return JsonResponse({'success': True})
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': str(e)})  





class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer


class Sensor_MQTTViewSet(viewsets.ModelViewSet):
    queryset = Sensor_MQTT.objects.all()
    serializer_class = Sensor_MQTTSerializer


class eventosCalendariosViewSet(viewsets.ModelViewSet):
    queryset = eventosCalendarios.objects.all()
    serializer_class = eventosCalendariosSerializer
    
class RutinaCodigoGViewSet(viewsets.ModelViewSet):
    queryset = RutinaCodigoG.objects.all()
    serializer_class =RutinaCodigoGSerializer

#Para empaquetar datos
from dateutil import parser
from datetime import datetime, timedelta

class DataDownloadView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start')
        end_date = request.query_params.get('end')
        
        if start_date and end_date:
            try:
                # Parseo las fechas y ajusto la fecha de finalización al final del día
                start_date = parser.parse(start_date)
                end_date = parser.parse(end_date)
                # Ajustar end_date al final del día
                end_date = end_date + timedelta(days=1) - timedelta(seconds=1)
            except ValueError:
                return HttpResponse("Invalid date format", status=400)

            # Filtrar los datos entre las fechas proporcionadas
            data = Sensor_MQTT.objects.filter(timestamp__range=[start_date, end_date])

            # Crear respuesta CSV
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="sensor_data.csv"'
            writer = csv.writer(response)
            writer.writerow(['timestamp', 'acelerometro_roll', 'acelerometro_pitch', 'acelerometro_yaw', 'giroscopio_roll', 'giroscopio_pitch', 'giroscopio_yaw', 'magnetometro_x', 'magnetometro_y', 'magnetometro_z', 'orientacion_roll', 'orientacion_pitch', 'orientacion_yaw', 'humedad', 'presion', 'temperatura'])
            
            for item in data:
                writer.writerow([item.timestamp, item.acelerometro_roll, item.acelerometro_pitch, item.acelerometro_yaw, item.giroscopio_roll, item.giroscopio_pitch, item.giroscopio_yaw, item.magnetometro_x, item.magnetometro_y, item.magnetometro_z, item.orientacion_roll, item.orientacion_pitch, item.orientacion_yaw, item.humedad, item.presion, item.temperatura])

            return response
        else:
            return HttpResponse("Start date and end date are required", status=400)




class DataAllDownloadView(APIView):
    # Se elimina la restricción de autenticación (si aún no lo has hecho)
    # permission_classes = [IsAuthenticated]  # Opcional: remover si no necesitas autenticación

    def get(self, request):
        # Obtener todos los datos de Sensor_MQTT
        data = Sensor_MQTT.objects.all()

        # Preparar respuesta HTTP con contenido CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_sensor_data.csv"'

        # Crear un objeto CSV writer y escribir la cabecera
        writer = csv.writer(response)
        writer.writerow(['timestamp', 'acelerometro_roll', 'acelerometro_pitch', 'acelerometro_yaw', 'giroscopio_roll', 'giroscopio_pitch', 'giroscopio_yaw', 'magnetometro_x', 'magnetometro_y', 'magnetometro_z', 'orientacion_roll', 'orientacion_pitch', 'orientacion_yaw', 'humedad', 'presion', 'temperatura'])
        
        # Escribir cada uno de los datos al CSV
        for item in data:
            writer.writerow([item.timestamp, item.acelerometro_roll, item.acelerometro_pitch, item.acelerometro_yaw, item.giroscopio_roll, item.giroscopio_pitch, item.giroscopio_yaw, item.magnetometro_x, item.magnetometro_y, item.magnetometro_z, item.orientacion_roll, item.orientacion_pitch, item.orientacion_yaw, item.humedad, item.presion, item.temperatura])

        return response
    