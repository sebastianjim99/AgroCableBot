from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings 
from django.contrib.staticfiles.urls import static


from .views import (Lineas_investigacionViewSet, ServiciosViewSet, ListCreateUsers, Login, RetrieveUpdateDestroyUsuarios, facultadesViewSet, programaViewSet, tipoIntegranteViewSet, integranteViewSet, proyectosViewSet, imagenesProyectosViewSet, videoProyectosViewSet)


router = DefaultRouter()
router.register('Lineas_investigacion', Lineas_investigacionViewSet, basename= 'Lineas_investigacion')
router.register('Servicios', ServiciosViewSet, basename= 'Servicios')
router.register('facultades', facultadesViewSet, basename= 'facultades')
router.register('programa', programaViewSet, basename= 'programa')
router.register('tipoIntegrante', tipoIntegranteViewSet, basename= 'tipoIntegrante')
router.register('integrante', integranteViewSet, basename= 'integrante')
router.register('imagenesProyectos', imagenesProyectosViewSet, basename= 'imagenesProyectos')
router.register('proyectos', proyectosViewSet, basename= 'proyectos')
router.register('videoProyectos', videoProyectosViewSet, basename= 'videoProyectos')

urlpatterns = [
    path('api/', include(router.urls)),
    path('list-create-Users/', ListCreateUsers.as_view(), name= 'list-create-Users'),
    path('loginView/', Login.as_view(), name='login'),
    path('retrieve-update-destroy-usarios/<int:pk>/', RetrieveUpdateDestroyUsuarios.as_view(), name= 'retrieve-update-destroy')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

