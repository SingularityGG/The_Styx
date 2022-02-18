from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Team, Scrim
from .serializers import ScrimSerializer, TeamSerializer

# Create your views here.
class TeamList(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queuryset = Team.objects.all()
    serializer_class = TeamSerializer

class ScrimList(ListCreateAPIView):
    queryset = Scrim.objects.all()
    serializer_class = ScrimSerializer

class ScrimDetail(RetrieveUpdateDestroyAPIView):
    queryset = Scrim.objects.all()
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    serializer_class = ScrimSerializer
    