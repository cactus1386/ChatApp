from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatClient(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = 'group_chat'
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name  # Fixed typo here as well
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']  # Use 'message'
        username = text_data_json['username']
        time = text_data_json['time']
        await self.channel_layer.group_send(
            self.roomGroupName,
            {
                'type': 'send_message',
                'message': message,  # Use 'message'
                'username': username,
                'time': time
            }
        )

    async def send_message(self, event):
        message = event['message']  # Use 'message'
        username = event['username']
        time = event['time']
        await self.send(text_data=json.dumps({
            'message': message,  # Use 'message'
            'username': username,
            'time': time
        }))
