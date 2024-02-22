from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('publish', views.publish_message, name='publish'),

    path('', include('imacuna.urls')),
    # path('', include('r_agrocablebot.urls')),

]

