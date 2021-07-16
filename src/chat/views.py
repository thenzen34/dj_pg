# chat/views.py
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    def get_template_names():
        is_mobile = getattr(request, 'Mobile_Agent')

        if is_mobile:
            return 'chat/mobile_index.html'
        return 'chat/index.html'

    return render(request, get_template_names(), {})


def test(request):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        'chat_123',
        {
            'type': 'chat_message',
            'message': 'hello from admin'
        })
    return HttpResponse('<p>Done</p>')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
