from django.db import models
from django.forms import modelformset_factory
from django.contrib.auth.models import User

# Create your models here.
class DiscordUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discord_id = models.CharField(max_length=128,default='not_provided')
    username = models.CharField(max_length = 128)
    discriminator = models.CharField(max_length=4)
    avatar = models.CharField(max_length=128)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=128)
    mfa_enabled = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    def __str__(self):
        return f'{self.discord_id}#{self.discriminator}'