from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings 
from django.contrib.staticfiles.urls import static


from .views import (Lineas_investigacionViewSet, ServiciosViewSet, ListCreateUsers, Login, RetrieveUpdateDestroyUsuarios)


router = DefaultRouter()
router.register('Lineas_investigacion', Lineas_investigacionViewSet, basename= 'Lineas_investigacion')
router.register('Servicios', ServiciosViewSet, basename= 'Servicios')

urlpatterns = [
    path('api/', include(router.urls)),
    path('list-create-Users/', ListCreateUsers.as_view(), name= 'list-create-Users'),
    path('loginView/', Login.as_view(), name='login'),
    path('retrieve-update-destroy-usarios/<int:pk>/', RetrieveUpdateDestroyUsuarios.as_view(), name= 'retrieve-update-destroy')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)