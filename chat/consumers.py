import json
import datetime
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.cache import caches, cache
from accounts.models import CustomUser

logger = logging.getLogger('consumer')

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        logger.info('User %s CONNECTED', self.scope['user'].username)

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        logger.info('User %s DISCONNECTED', self.scope['user'].username)
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from web socket
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )
    

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, room, message):

        #Get chached messages from room
        try:
            chached_messages = caches['default'].get(room)
            if chached_messages:
                chached_messages = json.loads(chached_messages)
                chached_messages.append({
                    'user':self.scope['user'].username,
                    'message':message,
                    'date':str(datetime.datetime.now())
                })
                cache.set(room,json.dumps(chached_messages))
            else:
                chached_messages = []
                chached_messages.append({
                    'user':self.scope['user'].username,
                    'message':message,
                })
                cache.set(room,json.dumps(chached_messages))
        except Exception as e:
            print('Error chaching the message: ',e)
            return False

        return True



