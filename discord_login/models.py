from django.db import models
from django.forms import modelformset_factory
from django.contrib.auth.models import User

# Create your models here.
class DiscordUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discord_id = models.BigIntegerField()
    username = models.CharField(max_length = 128)
    discriminator = models.IntegerField()
    avatar = models.CharField(max_length=128)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=128)
    mfa_enabled = models.CharField(max_length=128)
    last_login = models.DateTimeField()