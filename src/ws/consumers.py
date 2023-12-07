import asyncio
import json
import paho.mqtt.client as mqtt
from channels.generic.websocket import AsyncWebsocketConsumer

class BrokerConsumers(AsyncWebsocketConsumer):
    LORAMASTER2 = 'LORAMASTER2/output'

    async def connect(self):
        await self.accept()
        # Connect to MQTT broker
        self.mqtt_client = mqtt.Client()

        username = "admin"  # Replace with your MQTT broker username
        password = "Jimny8368"  # Replace with your MQTT broker password
        self.mqtt_client.username_pw_set(username, password)
        self.mqtt_client.connect("mqtt.ruanglab.com", 1883)
        self.mqtt_client.subscribe("data/KMI/BALI/SIMORLM2")
        self.mqtt_client.subscribe("data/KMI/BALI/SIMORLM1")
        self.mqtt_client.subscribe("data/KMI/BALI/SIMORLM3")
        self.mqtt_client.subscribe("LORAMASTER2/output")
        self.mqtt_client.subscribe("LORAMASTER3/output")
        self.mqtt_client.subscribe("pumpauto")
        self.mqtt_client.subscribe("Status_Auto_Pompa")
        self.mqtt_client.subscribe("test_ws")
        self.mqtt_client.on_message = self.on_mqtt_message
        self.mqtt_client.loop_start()

    def on_mqtt_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.send_message(payload))


    async def disconnect(self, close_code):
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if message := text_data_json.get('message'):
            if message == 'off':
                message = 0
            self.mqtt_client.publish(self.LORAMASTER2, message)
            response_message = f"Received message: {message}"
            await self.send(json.dumps({"message": response_message}))

    async def send_message(self, message):
        print(message)
        # Send a message to the WebSocket client
        await self.send(message)
