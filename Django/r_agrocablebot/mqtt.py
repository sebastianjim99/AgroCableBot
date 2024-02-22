import paho.mqtt.client as mqtt
from django.conf import settings
import json


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('sensores')
    else:
        print('Bad connection. Code:', rc)

    
def on_message(client, userdata, msg):
    from .models import Sensor_MQTT 
    try:
        data = json.loads(msg.payload.decode('utf-8'))
        Sensor_MQTT.objects.create(
            acelerometro_roll=data['acelerometro']['roll'],
            acelerometro_pitch=data['acelerometro']['pitch'],
            acelerometro_yaw=data['acelerometro']['yaw'],
            giroscopio_roll=data['giroscopio']['roll'],
            giroscopio_pitch=data['giroscopio']['pitch'],
            giroscopio_yaw=data['giroscopio']['yaw'],
            magnetometro_x=data['magnetometro']['x'],
            magnetometro_y=data['magnetometro']['y'],
            magnetometro_z=data['magnetometro']['z'],
            orientacion_roll=data['orientacion']['roll'],
            orientacion_pitch=data['orientacion']['pitch'],
            orientacion_yaw=data['orientacion']['yaw'],
            humedad=data['humedad']['value'],
            presion=data['presion']['value'],
            temperatura=data['temperatura']['value']
        )
    except Exception as e:
        print("Error al procesar y guardar los datos:", e)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
   
# client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)