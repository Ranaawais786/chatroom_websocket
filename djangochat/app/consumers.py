from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync, sync_to_async


class MySynConsumer(SyncConsumer):
    def websocket_Connect(self, event):
        print('websocket is connect', event)
        print('channel layer....', self.channel_layer)
        print('channel name....', self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            'programmer',
            self.channel_name)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_Receive(self, event):
        print('websocket is receive', event)
        print('websocket is receive', event['text'])
        print(' type of websocket is receive', type(event['text']))
        self.channel_layer.group_send('programmer', {
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self, event):
        print('Event', event)
        print('Acctual data', event['message'])
        print('Acctual data of type', type(event['message']))
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_Disconnect(self, event):
        print('websocket is disconnect', event)
        print('channel layer....', self.channel_layer)
        print('channel name....', self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            'programmer',
            self.channel_name)
        raise StopConsumer()
