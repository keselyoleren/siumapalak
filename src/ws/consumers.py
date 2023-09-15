import json
import paho.mqtt.client as mqtt
from channels.generic.websocket import AsyncWebsocketConsumer

class BrokerConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        # await self.accept()
        await self.channel_layer.group_add(
            'test',
            'test'
        )

        await self.accept()
        # Connect to MQTT broker
        self.mqtt_client = mqtt.Client()

        username = "admin"  # Replace with your MQTT broker username
        password = "Jimny8368"  # Replace with your MQTT broker password
        self.mqtt_client.username_pw_set(username, password)
        self.mqtt_client.connect("mqtt.ruanglab.com", 1883, 60)
        self.mqtt_client.subscribe("data/KMI/BALI/SIMORLM2")
        self.mqtt_client.subscribe("data/KMI/BALI/SIMORLM1")
        self.mqtt_client.subscribe("data/KMI/BALI/SIMORLM3")

        self.mqtt_client.on_message = self.on_mqtt_message
        self.mqtt_client.loop_forever()

        

    def on_mqtt_message(self, client, userdata, msg):
        # Handle MQTT messages
        payload = msg.payload.decode()
        print({"message": payload})
        # Send MQTT messages to WebSocket clients
        self.send(json.dumps({"message": payload}))

    async def disconnect(self, close_code):
        # Disconnect MQTT client when WebSocket is closed
        self.mqtt_client.disconnect()

    async def receive(self, text_data):
        # Handle messages received from WebSocket clients
        text_data_json = json.loads(text_data)
        print(text_data_json)
        if message := text_data_json.get('message'):
            # You can add your custom logic here to process the received message
            response_message = f"Received message: {message}"

            # Send a response back to the WebSocket client
            await self.send(json.dumps({"message": response_message}))
