from dis import dis
from django.urls import path
from .views import home, discord_login, discord_login_redirect

urlpatterns = [
    path("", home, name="0auth2"),
    path("login", discord_login, name="discord_login"),
    path("login/redirect", discord_login_redirect, name="discord_login_redirect")
]