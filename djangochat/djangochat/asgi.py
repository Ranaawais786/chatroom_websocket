import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from djangochat.app import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangochat.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket":
        URLRouter(
            routing.websocket_urlpatterns

    ),
})