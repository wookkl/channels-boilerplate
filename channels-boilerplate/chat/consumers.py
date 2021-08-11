from channels.generic.websocket import AsyncJsonWebsocketConsumer

from chat.handlers import ChatEventHandler


class ChatConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_handler = None

    async def connect(self):
        await super().connect()
        self.event_handler = ChatEventHandler(self)

    async def disconnect(self, code):
        await super().disconnect()

    async def receive_json(self, content, **kwargs):
        handler = self.event_handler.get_handler(content.pop('event'))
        if handler:
            await handler(content.get('data'))
