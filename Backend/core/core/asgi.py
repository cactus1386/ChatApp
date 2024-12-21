from channels.routing import ProtocolTypeRouter, URLRouter
from chat import router
from channels.auth import AuthMiddlewareStack
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                router.websocket_urlpatterns
            )
        )
    }
)