from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from the_styx.settings import DISCORD_APP_SECRET, DISCORD_REDIRECT, DISCORD_APP_ID

import requests
# Create your views here.

def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"msg":"Hello World!"})

def discord_login(request: HttpRequest):
    return redirect(DISCORD_REDIRECT)

def discord_login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    print(code)
    exchange_code(code)
    return JsonResponse({"msg":"Redirected"})

def exchange_code(code: str):
    data = {
        "client_id": DISCORD_APP_ID,
        "client_secret": DISCORD_APP_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/login/redirect",
        "scope": "identify"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post("https://discord.com/api/oauth2/token",data=data,headers=headers)
    print(response)
    credentials = response.json()
    print(credentials)