from django.contrib import admin

# Register your models here.

from .models import Usuarios, Lineas_investigacion, Servicios, facultades, programa,tipoIntegrante, integrante, proyectos, imagenesProyectos, videoProyectos 

admin.site.register(Usuarios)
admin.site.register(Lineas_investigacion)
admin.site.register(Servicios)
admin.site.register(facultades)  
admin.site.register(programa)  
admin.site.register(tipoIntegrante)  
admin.site.register(integrante)  
admin.site.register(proyectos)  
admin.site.register(imagenesProyectos)  
admin.site.register(videoProyectos)  