from rest_framework import viewsets, generics, permissions

from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .models import (
    acciones,
    tipoSensor,
    tipoCultivo,
    sensor,
    cultivo,
    plantas,
    imagenesxPlanta,
    calendarios,

)

from .serializers import (
    accionesSerializer,
    tipoSensorSerializer,
    tipoCultivoSerializer,
    sensorSerializer,
    cultivoSerializer,
    plantasSerializer,
    imagenesxPlantaSerializer,
    calendariosSerializer,
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

class plantasViewSet(viewsets.ModelViewSet):
    queryset = plantas.objects.all()
    serializer_class =plantasSerializer

class imagenesxPlantaViewSet(viewsets.ModelViewSet):
    queryset = imagenesxPlanta.objects.all()
    serializer_class =imagenesxPlantaSerializer

class calendariosViewSet(viewsets.ModelViewSet):
    queryset = calendarios.objects.all()
    serializer_class =calendariosSerializer