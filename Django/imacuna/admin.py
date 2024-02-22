from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Usuarios)
admin.site.register(Lineas_investigacion)
admin.site.register(Servicios)
admin.site.register(facultades)  
admin.site.register(programa)  
admin.site.register(tipoIntegrante)  
admin.site.register(integrante)  
class integrantesxProyecto(admin.ModelAdmin):
    filter_horizontal=['integrante','videoProyectos','imagenesProyectos']   

admin.site.register(proyectos,integrantesxProyecto)
admin.site.register(imagenesProyectos)  
admin.site.register(videoProyectos)  
