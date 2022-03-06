from dis import dis
from django.urls import path
from .views import home, discord_login

urlpatterns = [
    path("", home, name="0auth2"),
    path("login", discord_login, name="discord_login")
]