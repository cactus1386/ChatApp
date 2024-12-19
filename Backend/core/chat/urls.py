from django.urls import path
from .views import chat_view, home_view

urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('', home_view, name='home'),
]
