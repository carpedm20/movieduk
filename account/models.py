from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)
from django.db import models

class KerbUserManager(BaseUserManager):
  def create_user(self, email, synergy_level, password=None):
    user = self.model(email=email, synergy_level=synergy_level)
    return user

  def create_superuser(self, email, synergy_level, password):
    user = self.create_user(email, synergy_level, password=password)
    user.is_team_player = True
    user.save()
    return user

class DukUser(AbstractBaseUser):
  username = models.CharField(max_length=254, unique=True)
  first_name = models.CharField(max_length=30, blank=True)
  last_name = models.CharField(max_length=30, blank=True)
  email = models.EmailField(blank=True)
  synergy_level = models.IntegerField()
  is_team_player = models.BooleanField(default=False)

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email', 'synergy_level']
