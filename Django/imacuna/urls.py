from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings 
from django.contrib.staticfiles.urls import static
import views

from r_agrocablebot.views import (
    accionesViewSet,
    tiposensorViewSet,
    tipoCultivoViewSet,
    sensorViewSet,
    cultivoViewSet,
    plantasViewSet,
    imagenesxPlantaViewSet,
    calendariosViewSet,
)

from .views import (
    Lineas_investigacionViewSet, 
    ServiciosViewSet, 
    ListCreateUsers, 
    Login, 
    RetrieveUpdateDestroyUsuarios,
    cameras, 
    facultadesViewSet, 
    programaViewSet, 
    tipoIntegranteViewSet, 
    integranteViewSet, 
    proyectosViewSet, 
    imagenesProyectosViewSet, 
    videoProyectosViewSet,
    cameras,
    capturas, 
    )


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
#  ------------- AgroCableBot -----------

router.register('acciones', accionesViewSet, basename= 'acciones')
router.register('tiposensor', tiposensorViewSet, basename= 'tiposensor')
router.register('tipoCultivo', tipoCultivoViewSet, basename= 'tipoCultivo')
router.register('sensor', sensorViewSet, basename= 'sensor')
router.register('cultivo', cultivoViewSet, basename= 'cultivo')
router.register('plantas', plantasViewSet, basename= 'plantas')
router.register('imagenesxPlanta', imagenesxPlantaViewSet, basename= 'imagenesxPlanta')
router.register('calendarios', calendariosViewSet, basename= 'calendarios')

urlpatterns = [
    path('api/', include(router.urls)),
    path('list-create-Users/', ListCreateUsers.as_view(), name= 'list-create-Users'),
    path('loginView/', Login.as_view(), name='login'),
    path('retrieve-update-destroy-usarios/<int:pk>/', RetrieveUpdateDestroyUsuarios.as_view(), name= 'retrieve-update-destroy'),
    # ------------ camara -----------
    path('aboveCam/', cameras , name='aboveCamera'),
    path('aboveCam2/', cameras , name='aboveCamera2'),
    path('captura/', capturas , name='captura')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)