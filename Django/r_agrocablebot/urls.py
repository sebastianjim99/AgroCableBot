from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings 
from django.contrib.staticfiles.urls import static


from .views import (
    accionesViewSet,
    tiposensorViewSet,
    tipoCultivoViewSet,
    sensorViewSet,
    cultivoViewSet,
    plantasViewSet,
    imagenesxPlantaViewSet,
    calendariosViewSet,
   )

router = DefaultRouter()
router.register('acciones', accionesViewSet, basename= 'acciones')
router.register('tiposensor', tiposensorViewSet, basename= 'tiposensor')
router.register('tipoCultivo', tipoCultivoViewSet, basename= 'tipoCultivo')
router.register('sensor', sensorViewSet, basename= 'sensor')
router.register('cultivo', cultivoViewSet, basename= 'cultivo')
router.register('plantas', plantasViewSet, basename= 'plantas')
router.register('imagenesxPlanta', imagenesxPlantaViewSet, basename= 'imagenesxPlanta')
router.register('calendarios', calendariosViewSet, basename= 'calendarios')

urlpatterns = [
    path('Agrocablebot_Api/', include(router.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

