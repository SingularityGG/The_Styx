from rest_framework import serializers
from .models import Scrim, Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class ScrimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrim
        fields = "__all__"