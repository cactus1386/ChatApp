from django.shortcuts import render
from .models import Chat

# Create your views here.


def chat_view(request):
    massages = Chat.objects.all()
    return render(request, 'chat/chat.html', {'massages': massages})


def home_view(request):
    return render(request, 'home.html')
