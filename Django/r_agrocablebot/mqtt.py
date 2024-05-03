# import paho.mqtt.client as mqtt
# from django.conf import settings
# import json
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def on_connect(mqtt_client, userdata, flags, rc):
#     if rc == 0:
#         print('Connected successfully')
#         mqtt_client.subscribe('sensores')
#         mqtt_client.subscribe('comandos')
#     else:
#         print('Bad connection. Code:', rc)
   
# def on_message(client, userdata, msg):
#     from .models import Sensor_MQTT 
#     try:
#         data = json.loads(msg.payload.decode('utf-8'))
#         Sensor_MQTT.objects.create(
#             acelerometro_roll=data['acelerometro']['roll'],
#             acelerometro_pitch=data['acelerometro']['pitch'],
#             acelerometro_yaw=data['acelerometro']['yaw'],
#             giroscopio_roll=data['giroscopio']['roll'],
#             giroscopio_pitch=data['giroscopio']['pitch'],
#             giroscopio_yaw=data['giroscopio']['yaw'],
#             magnetometro_x=data['magnetometro']['x'],
#             magnetometro_y=data['magnetometro']['y'],
#             magnetometro_z=data['magnetometro']['z'],
#             orientacion_roll=data['orientacion']['roll'],
#             orientacion_pitch=data['orientacion']['pitch'],
#             orientacion_yaw=data['orientacion']['yaw'],
#             humedad=data['humedad']['value'],
#             presion=data['presion']['value'],
#             temperatura=data['temperatura']['value']
#         )
#     except Exception as e:
#         print("Error al procesar y guardar los datos:", e)

# def publish(cliente,topic,message):
#     result = cliente.publish(topic, json.dumps(message))

# client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
# client.on_connect = on_connect
# client.on_message = on_message
# client.username_pw_set(os.environ['MQTT_USER'], os.environ['MQTT_PASSWORD'])

# try:
#     # Intentar conectar al servidor MQTT
#     client.connect(
#         host=os.environ['MQTT_SERVER'],
#         port=int(os.environ['MQTT_PORT']),
#         keepalive=int(os.environ['MQTT_KEEPALIVE']),
#     )
#     # Comenzar el bucle de escucha de MQTT
#     client.loop_start()
# except Exception as e:
#     print("No se pudo conectar al servidor MQTT:", e)

import os
import uuid
import json
from django.db import IntegrityError
from json import dumps, loads
import paho.mqtt.client as mqtt
from .mqtt_utils import logger, singleton
from dotenv import load_dotenv

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
        self.__client.connect(os.environ['MQTT_SERVER'], int(os.environ['MQTT_PORT']))
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message
        self.__client.on_publish = self.__on_publish
        self.__client.username_pw_set(os.environ['MQTT_USER'], os.environ['MQTT_PASSWORD'])
        # self.__client.on_disconnect = self.__on_disconnect
    #    REVISAR
        # try:
        #     self.__client.connect(os.environ['MQTT_SERVER'], int(os.environ['MQTT_PORT']))
        #     self.__client.loop_start()
        # except Exception as e:
        #     print("No se pudo conectar al servidor MQTT:", e)
    # ----------
        self.topics = {'comandos' : self.__comandos, 'status' : self.__status}
        self.interfaceCommands = {'send_data' : self.send_data, 'send_aio' : self.send_aio}
        self.last_position = {'x' : 0, 'y' : 0, 'z' : 0}
        self.__client.loop_start()  # ojito esto estaba comentando.   


    def __on_connect(self, client, userdata, flags, rc):
        """
        Método de devolución de llamada para manejar la conexión exitosa al servidor MQTT.
        """
        if rc == 0:
            print('Connected successfully')
            self.__client.subscribe('comandos')
            self.__client.subscribe('status')
            self.__client.subscribe('sensores')
            self.__client.publish('testingimacuna', 'pos si se conectó')
        else:
            print('Bad connection. Code:', rc)
        
        # self.__client.subscribe('comandos')
        # self.__client.subscribe('status')
        # self.__client.subscribe('sensores')
        # self.__client.publish('testingimacuna', 'pos si se conectó')
        # print("Conexion correcta con el servidor mqtt")

    def __on_message(self, client, userdata, msg):
        """
        Método de devolución de llamada para manejar mensajes MQTT entrantes.
        """
        from .models import Sensor_MQTT 
        import json
        print(f"Recibido mensaje en tópico {msg.topic} con QoS {msg.qos}")
        
        try:
            data = json.loads(msg.payload.decode('utf-8'))
            # Logging para verificar el contenido recibido
            print(f"Datos recibidos: {data}")

            obj, created = Sensor_MQTT.objects.get_or_create(
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
            if created:
                print("Datos guardados correctamente")
            else:
                print("El registro ya existía y no se duplicó.")

        except Exception as e:
            print("Error al procesar y guardar los datos:", e)

    def __on_publish(self, client, userdata, result):
        pass

    def __on_disconnect(self, client, userdata, rc):
        pass
    
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
        self.__client.publish(topic, message)

MqttClient()