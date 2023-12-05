from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


from .views import Lineas_investigacionViewSet, ServiciosViewSet

router = DefaultRouter()
router.register('Lineas_investigacion', Lineas_investigacionViewSet, basename= 'Lineas_investigacion')
router.register('Servicios', ServiciosViewSet, basename= 'Servicios')

urlpatterns = [

    path('api/', include(router.urls)),
]