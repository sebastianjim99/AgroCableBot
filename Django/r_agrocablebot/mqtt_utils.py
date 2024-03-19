import paho.mqtt.publish as publish
import json
import os

def publicar_mensaje_mqtt(topic, message):
    try:
        # Definir las credenciales del cliente MQTT si es necesario
        auth = {
            'username': os.environ.get('MQTT_USER'),
            'password': os.environ.get('MQTT_PASSWORD')
        }

        # Convertir el mensaje a formato JSON
        json_message = json.dumps(message)

        # Publicar el mensaje MQTT en el tema especificado
        publish.single(topic, json_message, hostname=os.environ.get('MQTT_SERVER'), port=int(os.environ.get('MQTT_PORT')), auth=auth)
        
        return True  # Indica que el mensaje se publicó correctamente
    except Exception as e:
        print("Error al publicar el mensaje MQTT:", e)
        return False  # Indica que ocurrió un error al publicar el mensaje
