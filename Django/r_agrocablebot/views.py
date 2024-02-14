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