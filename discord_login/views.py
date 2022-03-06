from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from the_styx.settings import DISCORD_REDIRECT
# Create your views here.

def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"msg":"Hello World!"})

def discord_login(request: HttpRequest):
    return redirect(DISCORD_REDIRECT)