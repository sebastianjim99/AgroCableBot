from django.utils import timezone
from .models import eventosCalendarios
from celery import shared_task
from .mqtt_utils import publicar_mensaje_mqtt  


@shared_task
def ejecutar_evento_programado():
    ahora = timezone.localtime(timezone.now())  # Convertir la hora actual a la zona horaria local

    # Obtener el evento más cercano a la hora actual que aún no ha ocurrido
    evento_mas_cercano = eventosCalendarios.objects.filter(start__gte=ahora).order_by('start').first()
    

    if evento_mas_cercano:
        # Si la fecha y hora del evento coinciden con la fecha y hora actual, ejecutar el evento
        if evento_mas_cercano.start == ahora:
            ejecutar_evento.delay(evento_mas_cercano.id)  # Usamos .delay() para programar la tarea
            topic = "comandos"
            message = {'interface': 'send_aio'}
            publicar_mensaje_mqtt(topic, message) # Llamar a la función para enviar mensaje MQTT
            evento_mas_cercano.delete()  # Eliminar el evento después de ejecutarlo
            

        # Calcular el tiempo de espera hasta la hora de inicio del evento
        tiempo_espera = evento_mas_cercano.start - ahora

        # Programar la ejecución de la tarea para la hora de inicio del evento
        ejecutar_evento.apply_async(args=[evento_mas_cercano.id], countdown=tiempo_espera.total_seconds())
        # Convertir la hora del evento a la zona horaria local
        hora_evento_local = evento_mas_cercano.start.astimezone(timezone.get_current_timezone())

        return f"La proxima tarea a ejecutar es '{evento_mas_cercano.title}' a las {hora_evento_local}"

    else:
        return "No hay eventos pendientes en este momento"

@shared_task
def ejecutar_evento(evento_id):
    evento = eventosCalendarios.objects.get(id=evento_id)
    # Aquí ejecuta la acción asociada al evento
    return f"Ejecutando evento '{evento.title}'" 

