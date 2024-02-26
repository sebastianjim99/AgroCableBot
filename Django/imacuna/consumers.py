from channels.generic.websocket import AsyncWebsocketConsumer
import json

class SensorDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Procesa el mensaje recibido (si es necesario)
        data = json.loads(text_data)
        
        # Aquí podrías procesar los datos y enviar una respuesta si es necesario
        # Por ejemplo, podrías realizar una consulta a la base de datos y enviar los resultados
        
        # En este ejemplo, simplemente reenviamos los datos recibidos a todos los clientes conectados
        await self.send(text_data=json.dumps(data))