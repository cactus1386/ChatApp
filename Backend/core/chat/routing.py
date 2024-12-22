from django.urls import path, include
from .consumer import ChatClient


websocket_urlpatterns = [
    path("", ChatClient.as_asgi())
]
