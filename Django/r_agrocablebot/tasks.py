# import paho.mqtt.publish as publish
import json
from .models import eventosCalendarios,Sensor_MQTT
from django.utils import timezone
from celery import shared_task
from .mqtt import mqtt_client
# Para el empaquetamiento y envio periodico de datos
# from django.core.mail import EmailMessage


@shared_task
def ejecutar_evento_programado():
    ahora = timezone.localtime(timezone.now())

    evento_mas_cercano = eventosCalendarios.objects.filter(start__gte=ahora).order_by('start').first()

    if evento_mas_cercano:
        if evento_mas_cercano.start == ahora:
            # publish_message()
            ejecutar_evento.delay(evento_mas_cercano.id)
            evento_mas_cercano.delete()

        tiempo_espera = evento_mas_cercano.start - ahora
        ejecutar_evento.apply_async(args=[evento_mas_cercano.id], countdown=tiempo_espera.total_seconds())
        hora_evento_local = evento_mas_cercano.start.astimezone(timezone.get_current_timezone())

        return f"La próxima tarea a ejecutar es '{evento_mas_cercano.title}' a las {hora_evento_local}"
    else:
        return "No hay eventos pendientes en este momento"


@shared_task
def ejecutar_evento(evento_id):
    try:
        evento = eventosCalendarios.objects.get(id=evento_id)
        mqtt_client.connect()  # Asegurarse de que el cliente esté conectado
        mqtt_client.publish('comandos', json.dumps({'interface': 'send_aio'}))  # Publicar el mensaje MQTT
        return f"Ejecutando evento '{evento.title}'"
    except eventosCalendarios.DoesNotExist:
        return f"El evento con ID '{evento_id}' no existe"
    except Exception as e:
        return f"Se produjo un error al ejecutar el evento: {str(e)}"
