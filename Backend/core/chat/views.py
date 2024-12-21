from django.shortcuts import render, redirect
from django.http import JsonResponse


def chat(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chat.html", context)


def home_view(request):
    return render(request, 'home.html')
