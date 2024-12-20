from django.urls import path
from .views import chat, home_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home_view, name='home'),
    path('chat/', chat, name='chat'),
    path("auth/login/", LoginView.as_view
         (template_name="chat/loginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
