from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
# Create your models here.

class Game(models.Model):
    name:str = models.CharField(32)
    def __str__(self):
        return self.name


class Team(models.Model):
    date_created:datetime = models.DateTimeField(default=datetime.now)
    name:str = models.CharField(32)
    elo:int = models.IntegerField()
    owner = models.ForeignKey(
        get_user_model(), on_delete=CASCADE, null=False
    )
    game:Game = models.ForeignKey(Game, on_delete=models.PROTECT)
    rating:float = models.FloatField(default=5.0)
    def __str__(self):
        return f'{self.name}: {self.elo} | ({round(self.rating,2)}/5)'


class Scrim(models.Model):
    posted:datetime = models.DateTimeField(default=datetime.now)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False
    )
    responses:list = models.JSONField(default=list)
    team:Team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_time:datetime = models.DateTimeField(null=False)
    end_time:datetime = models.DateTimeField(null=False)
    status:str = models.CharField(choices=(("CANCELED","Canceled"),("SCHEDULED","Scheduled"),("COMPLETED","Completed")))
    def __str__(self):
        return f'Team: {self.team.name} \nTeam ELO: {self.team.elo}\n Team Rating: {self.team.rating} \nStart Time: {self.start_time} \nEnd Time: {self.end_time}'