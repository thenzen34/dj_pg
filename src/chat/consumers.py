import json

# from django.contrib.contenttypes.models import ContentType

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from django.db.models import QuerySet


class MessagePack:
    def __init__(self, type_id, value):
        self.type_id = type_id
        self.value = value

    @staticmethod
    def from_dict(obj: dict) -> 'MessagePack':
        assert isinstance(obj, dict)
        type_id = obj.get("typeId")
        value = obj.get("value")
        return MessagePack(type_id, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["typeId"] = self.type_id
        result["value"] = self.value
        return result


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # APPP

    # общая точка входа
    # Receive message from WebSocket
    async def receive_json(self, content, **kwargs):
        message = MessagePack.from_dict(content)

        print(message.type_id, message.value)

        for handler in self.handlers.get(message.type_id, []):
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': handler.__name__,
                    'message': message.value
                }
            )

    # событие1
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send_json({
            'r': 'chat_message',
            'message': message
        })

    # событие3
    # Receive message from room group
    async def chat_speed(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send_json({
            'r': 'chat_speed',
            'message': message
        })

    # событие2
    # Receive message from room group
    async def chat_checkbox(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send_json({
            'r': 'chat_checkbox',
            'message': message
        })

    # событие на клик
    # Receive message from room group
    async def click(self, event):
        print('click here')
        message = event['message']

        # Send message to WebSocket
        await self.send_json({
            'r': 'click',
            'message': message
        })

    handlers = {
        'message': [chat_message],
        'checkbox': [chat_checkbox],
        'speed': [chat_speed],
        'click': [click],
    }
