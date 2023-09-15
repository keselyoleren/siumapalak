from operator import imod
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from ws import consumers
from ws.routing import websocket_urlpatterns as url
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


application = ProtocolTypeRouter({
    'websocket': 
    URLRouter(url)
})