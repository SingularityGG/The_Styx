from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Game
from .serializers import GameSerializer

# Create your views here.
class GameList(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer