from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from rest_framework.response import Response

from .serializers import Lineas_investigacionSerializer, ServiciosSerializer, serializers

from .models import Lineas_investigacion, Servicios
# Create your views here.


class Lineas_investigacionViewSet(viewsets.ModelViewSet):
    queryset = Lineas_investigacion.objects.all()
    serializer_class = Lineas_investigacionSerializer


class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer
    


            