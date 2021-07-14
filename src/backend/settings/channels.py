from .settings import *

INSTALLED_APPS.append('channels')
INSTALLED_APPS.append('chat')

ASGI_APPLICATION = "backend.asgi.application"

CHANNEL_LAYERS_BACKEND = os.getenv('CHANNEL_LAYERS_BACKEND', False)

if CHANNEL_LAYERS_BACKEND:
    REDIS_URL = os.getenv('REDIS_URL')
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': CHANNEL_LAYERS_BACKEND,
            'CONFIG': {
                "hosts": [REDIS_URL],
            },
        },
    }
else:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels.layers.InMemoryChannelLayer',
        },
    }
