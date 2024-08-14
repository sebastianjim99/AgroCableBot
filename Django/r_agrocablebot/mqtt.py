import os
import uuid
import json
from django.db import IntegrityError
from json import dumps, loads
import paho.mqtt.client as mqtt
from .mqtt_utils import logger, singleton
from dotenv import load_dotenv

from datetime import datetime, timedelta

load_dotenv()
@singleton
class MqttClient:
    """
    Clase para manejar un cliente MQTT.

    Esta clase proporciona métodos para conectar y comunicarse con un servidor MQTT, así como para manejar mensajes recibidos.

    Attributes:
    __client (mqtt.Client): Cliente MQTT para la comunicación con el servidor.
    sense (SenseHat): Instancia de SenseHat para obtener datos de sensores.
    topics (dict): Diccionario que mapea nombres de topics MQTT a métodos de manejo de mensajes.
    interfaceCommands (dict): Diccionario que mapea nombres de comandos de interfaz a métodos de la instancia.
    last_position (dict): Última posición registrada del dispositivo.
    """
    def __init__(self):
        """
        Inicializa el cliente MQTT y otros atributos.
        """
        self.__client = mqtt.Client(
            client_id=f'apiClient-{uuid.uuid4()}', 
            clean_session=True,
            userdata=None,
            protocol=mqtt.MQTTv311,
            transport='tcp'
            )

        self.__client.username_pw_set(os.environ['MQTT_USER'], os.environ['MQTT_PASSWORD'])
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message
        self.__client.on_publish = self.__on_publish
        self.__client.on_disconnect = self.__on_disconnect
        self.connected = False   # -----------AGG
        self.connected_once = False    # -----------AGG}
        self.last_message_time = None  # -----------AGG}

    #    REVISAR
        # try:
        #     self.__client.connect(os.environ['MQTT_SERVER'], int(os.environ['MQTT_PORT']))
        #     self.__client.loop_start()
        # except Exception as e:
        #     print("No se pudo conectar al servidor MQTT:", e)
    # ----------
        self.topics = {
            'comandos' : self.__comandos, 
            'status' : self.__status
        }
        self.interfaceCommands = {
            'send_data' : self.send_data, 
            'send_aio' : self.send_aio
        }
        self.last_position = {'x' : 0, 'y' : 0, 'z' : 0}
        self.connected = False

        # self.__client.loop_start()  # ojito esto estaba comentando.   

    def connect(self):
        """
        Intenta conectar el cliente al servidor MQTT.
        """
        if not self.connected: # -----------AGG
            try:
                self.__client.connect(os.environ['MQTT_SERVER'], int(os.environ['MQTT_PORT']))
                self.__client.loop_start()
                self.connected = True
                print("Connected successfully")
            except Exception as e:
                print(f"Could not connect to MQTT server: {e}")
                self.connected = False


    def __on_connect(self, client, userdata, flags, rc):
        """
        Método de devolución de llamada para manejar la conexión exitosa al servidor MQTT.
        """
        if rc == 0:
            if not self.connected_once:  # -----------AGG
                print('Connected successfully')
                self.__client.subscribe('comandos')
                self.__client.subscribe('status')
                self.__client.subscribe('sensores')
                self.__client.publish('testingimacuna', 'pos si se conectó')
                self.connected_once = True
        else:
            print('Bad connection. Code:', rc)



    def __on_message(self, client, userdata, msg):
        """
        Método de devolución de llamada para manejar mensajes MQTT entrantes.
        """
        from .models import Sensor_MQTT 
        import json
        print(f"Recibido mensaje en tópico {msg.topic} con QoS {msg.qos}")
        
        # try:
        #     data = json.loads(msg.payload.decode('utf-8'))
        #     # Logging para verificar el contenido recibido
        #     print(f"Datos recibidos: {data}")

        #     obj, created = Sensor_MQTT.objects.get_or_create(
        #         acelerometro_roll=data['acelerometro']['roll'],
        #         acelerometro_pitch=data['acelerometro']['pitch'],
        #         acelerometro_yaw=data['acelerometro']['yaw'],
        #         giroscopio_roll=data['giroscopio']['roll'],
        #         giroscopio_pitch=data['giroscopio']['pitch'],
        #         giroscopio_yaw=data['giroscopio']['yaw'],
        #         magnetometro_x=data['magnetometro']['x'],
        #         magnetometro_y=data['magnetometro']['y'],
        #         magnetometro_z=data['magnetometro']['z'],
        #         orientacion_roll=data['orientacion']['roll'],
        #         orientacion_pitch=data['orientacion']['pitch'],
        #         orientacion_yaw=data['orientacion']['yaw'],
        #         humedad=data['humedad']['value'],
        #         presion=data['presion']['value'],
        #         temperatura=data['temperatura']['value']
        #     )
        #     if created:
        #         print("Datos guardados correctamente")
        #     else:
        #         print("El registro ya existía y no se duplicó.")

        # except Exception as e:
        #     print("Error al procesar y guardar los datos:", e)
        try:
            data = json.loads(msg.payload.decode('utf-8'))
            timestamp_str = data['timestamp']['fecha']
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            # Verifica si el mensaje llega en el mismo segundo o en un intervalo pequeño
            if self.last_message_time and (timestamp - self.last_message_time) < timedelta(seconds=2):
                print("Mensaje descartado por ser repetido en el mismo segundo")
                return

            # Actualiza el tiempo del último mensaje
            self.last_message_time = timestamp

            # Aquí sigue tu lógica para guardar o promediar los datos...
            Sensor_MQTT.objects.create(
                timestamp=timestamp,
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
            print(f"Nuevo registro creado en {timestamp}")

        except Exception as e:
            print("Error al procesar y guardar los datos:", e)

    def __on_publish(self, client, userdata, result):
        pass

    def __on_disconnect(self, client, userdata, rc):
        print(f"Disconnected with result code: {rc}")
        self.connected = False
    
    def __comandos(self, message):
        """
        Método para manejar los mensajes recibidos en el topic 'comandos'.
        """
        if message.get('interface'):
            pass
            self.interfaceCommands[message['interface']]()
            

    def __status(self, message):
        """
        Método para manejar los mensajes recibidos en el topic 'status'.
        """
        if (any(key in ['x', 'y', 'z'] for key in message.keys())):
            self.last_position = message

    
    
    def send_aio(self):
        """
        Método para publicar datos de sensores en un topic MQTT llamado 'sensores'.
        """
        pass

    def send_data(self):
        """
        Método para publicar datos de sensores en topics MQTT específicos y guardar los datos en la base de datos.
        """
        pass

    def publish(self, topic, message):
        """
        Método para publicar un mensaje MQTT en un topic específico.
        """
        #comente ----
        # if not self.connected:
        #     self.connect()
        # self.__client.publish(topic, message)
        #-----
        self.connect()  # Asegura la conexión antes de publicar
        self.__client.publish(topic, message)

mqtt_client = MqttClient()