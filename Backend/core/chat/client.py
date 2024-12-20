from channels.generic.websocket import AsyncWebSocketConsumer
import json


class ChatClient(AsyncWebSocketConsumer):
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
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        massage = text_data_json['massage']
        username = text_data_json['username']
        time = text_data_json['time']
        await self.channel_layer.group_send(
            self.roomGroupName,
            {
                'type': 'sendMassage',
                'massage': massage,
                'username': username,
                'time': time
            })

    async def sendMassage(self, event):
        massage = event['massage']
        username = event['username']
        time = event['time']
        await self.send(text_data=json.dumps({
            'massage': massage,
            'username': username,
            'time': time
        }))
