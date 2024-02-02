from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(acciones)
admin.site.register(tipoSensor)
admin.site.register(tipoCultivo)

class sensoresxCultivo(admin.ModelAdmin):
    filter_horizontal=['sensores',]   

admin.site.register(cultivo,sensoresxCultivo) 
class plantasxCalendario(admin.ModelAdmin):
    filter_horizontal=['plantas',]   

admin.site.register(calendarios,plantasxCalendario) 
admin.site.register(plantas)  
admin.site.register(sensor)  
admin.site.register(imagenesxPlanta)  
# admin.site.register(tablasEstadisticas)  
# admin.site.register(graficos)  
# admin.site.register(estadisticas) 
#admin.site.register(mo_agroCableBot)  


