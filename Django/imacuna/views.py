from rest_framework import viewsets, generics, permissions

from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import Lineas_investigacionSerializer, ServiciosSerializer, UsersSerializer, facultadesSerializer, programaSerializer, tipoIntegranteSerializer, integranteSerializer, proyectosSerializer, imagenesProyectosSerializer, videoProyectosSerializer

from .models import Lineas_investigacion, Servicios, Usuarios, facultades, programa,tipoIntegrante, integrante, proyectos, imagenesProyectos, videoProyectos 
# Create your views here.

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, "user_id": user.id})


class ListCreateUsers(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UsersSerializer

class RetrieveUpdateDestroyUsuarios(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Usuarios.objects.all()
    serializer_class = UsersSerializer


class Lineas_investigacionViewSet(viewsets.ModelViewSet):
    queryset = Lineas_investigacion.objects.all()
    serializer_class = Lineas_investigacionSerializer


class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer

class facultadesViewSet(viewsets.ModelViewSet):
    queryset = facultades.objects.all()
    serializer_class = facultadesSerializer

    def get_queryset(self):
        return facultades.objects.filter(nombre=self.request.facultades_id)

class programaViewSet(viewsets.ModelViewSet):
    queryset = programa.objects.all()
    serializer_class = programaSerializer

class tipoIntegranteViewSet(viewsets.ModelViewSet):
    queryset =  tipoIntegrante.objects.all()
    serializer_class = tipoIntegranteSerializer

class integranteViewSet(viewsets.ModelViewSet):
    queryset = integrante.objects.all()
    serializer_class = integranteSerializer

class proyectosViewSet(viewsets.ModelViewSet):
    queryset = proyectos.objects.all()
    serializer_class = proyectosSerializer

class imagenesProyectosViewSet(viewsets.ModelViewSet):
    queryset = imagenesProyectos.objects.all()
    serializer_class = imagenesProyectosSerializer

class videoProyectosViewSet(viewsets.ModelViewSet):
    queryset = videoProyectos.objects.all()
    serializer_class = videoProyectosSerializer
