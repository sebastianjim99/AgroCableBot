from django.contrib import admin

# Register your models here.

from .models import Usuarios, Lineas_investigacion, Servicios

admin.site.register(Usuarios)
admin.site.register(Lineas_investigacion)
admin.site.register(Servicios)