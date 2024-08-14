# import paho.mqtt.publish as publish
import json
from .models import eventosCalendarios,Sensor_MQTT
from django.utils import timezone
from celery import shared_task
from .mqtt import mqtt_client
# Para el empaquetamiento y envio periodico de datos
from django.core.mail import EmailMessage
import csv
from io import StringIO
from django.conf import settings


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
        if not mqtt_client.connected:
            mqtt_client.connect()
            print("Reconexion")
        
        # mqtt_client.connect()  # Asegurarse de que el cliente esté conectado
        mqtt_client.publish('comandos', json.dumps({'interface': 'send_aio'}))  # Publicar el mensaje MQTT
        return f"Ejecutando evento '{evento.title}'"
    except eventosCalendarios.DoesNotExist:
        return f"El evento con ID '{evento_id}' no existe"
    except Exception as e:
        return f"Se produjo un error al ejecutar el evento: {str(e)}"


# Empaquetamiento y envio de datos 
@shared_task
def send_data_via_email():
    # Recopilar todos los datos
    data = Sensor_MQTT.objects.all()

    # Crear un archivo CSV en memoria
    csvfile = StringIO()
    writer = csv.writer(csvfile)
    writer.writerow(['timestamp', 'acelerometro_roll', 'acelerometro_pitch', 'acelerometro_yaw', 'giroscopio_roll', 'giroscopio_pitch', 'giroscopio_yaw', 'magnetometro_x', 'magnetometro_y', 'magnetometro_z', 'orientacion_roll', 'orientacion_pitch', 'orientacion_yaw', 'humedad', 'presion', 'temperatura'])

    for item in data:
        writer.writerow([item.timestamp, item.acelerometro_roll, item.acelerometro_pitch, item.acelerometro_yaw, item.giroscopio_roll, item.giroscopio_pitch, item.giroscopio_yaw, item.magnetometro_x, item.magnetometro_y, item.magnetometro_z, item.orientacion_roll, item.orientacion_pitch, item.orientacion_yaw, item.humedad, item.presion, item.temperatura])

    # Mover al principio del archivo para preparar la lectura
    csvfile.seek(0)

    # Enviar el email con el archivo CSV adjunto usando configuraciones de Django
    email = EmailMessage(
        'AgroCableBot - Datos de los Últimos Tres Meses',
        'Aquí están los datos de los sensores de los últimos tres meses.',
        settings.DEFAULT_FROM_EMAIL,  # Usa el remitente por defecto configurado en Django
        ['semillero.imacuna@gmail.com']  # Asegúrate de cambiar esto a la dirección de correo real deseada
    )
    email.attach('data.csv', csvfile.getvalue(), 'text/csv')
    email.send()
    return "Enviando paquete de datos"