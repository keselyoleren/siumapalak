from django.urls import re_path, path

from ws import consumers

websocket_urlpatterns = [
    re_path(r'ws/mqtt$', consumers.BrokerConsumers),
]
