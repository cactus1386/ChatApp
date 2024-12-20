from django.urls import path
from .views import chat, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('chat/', chat, name='chat'),
]
