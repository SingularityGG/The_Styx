from django.urls import path
from .views import GameDetail, GameList

urlpatterns = [
    path("", GameList.as_view(), name="game_list"),
    path("game/<int:pk>/", GameDetail.as_view(), name="game_detail")
]