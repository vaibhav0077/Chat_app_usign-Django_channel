from django.urls import path
from . import consumers

websocke_patterns  = [
    path('', consumers.ChatConsumer.as_asgi())
]