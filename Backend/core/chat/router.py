from django.urls import path, include
from .client import ChatClient


websocket_urlpatterns = [
    path("", ChatClient.as_asgi())
]
