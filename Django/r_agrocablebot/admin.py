from django.contrib import admin
from django import forms
from .models import *
# Register your models here.

admin.site.register(acciones)
admin.site.register(tipoSensor)
admin.site.register(sensor)
admin.site.register(tipoCultivo)

class sensoresxCultivo(admin.ModelAdmin):
    filter_horizontal=['sensores',]   

admin.site.register(cultivo,sensoresxCultivo) 
# class plantasxCalendario(admin.ModelAdmin):
#     filter_horizontal=['plantas','cultivo',]   

# admin.site.register(calendarios,plantasxCalendario) 

class CalendarioAdmin(admin.ModelAdmin):
    def get_cultivo(self, obj):
        return ", ".join([cultivo.nombre for cultivo in obj.cultivo.all()])
    get_cultivo.short_description = 'cultivo'

    def get_planta(self, obj):
        return ", ".join([plantas.nombre for plantas in obj.plantas.all()])
    get_planta.short_description = 'plantas'
    
    list_display = ['acciones', 'get_cultivo', 'get_planta', 'fecha_inicio', 'repeticion']
    list_filter = ['repeticion']
    filter_horizontal = ['cultivo','plantas']
    search_fields = ['acciones__nombre']
admin.site.register(calendarios, CalendarioAdmin)
admin.site.register(plantas)  
admin.site.register(imagenesxPlanta)  
# admin.site.register(tablasEstadisticas)  
# admin.site.register(graficos)  
# admin.site.register(estadisticas) 
#admin.site.register(mo_agroCableBot)  

admin.site.register(Sensor_MQTT)
admin.site.register(eventosCalendarios)


