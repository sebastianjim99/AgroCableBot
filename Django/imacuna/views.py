from rest_framework import viewsets, generics, permissions

from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import Lineas_investigacionSerializer, ServiciosSerializer, UsersSerializer

from .models import Lineas_investigacion, Servicios, Usuarios
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

    def get_queryset(self):
        return Usuarios.objects.filter(user=self.request.user)

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
    
