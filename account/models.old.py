from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager

import urllib2
from django.contrib.auth import authenticate

from django.contrib.auth.models import UserManager

class FacebookSessionError(Exception):
    def __init__(self, error_type, message):
        self.message = message
        self.type = error_type
    def get_message(self):
        return self.message
    def get_type(self):
        return self.type
    def __unicode__(self):
        return u'%s: "%s"' % (self.type, self.message)

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(username=username)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password)
        user.is_team_player = True
        user.save()
        return use

class DukUser(AbstractBaseUser):
  username = models.CharField(max_length=30, unique=True)
  first_name = models.CharField(max_length=30, blank=True)
  last_name = models.CharField(max_length=30, blank=True)
  email = models.EmailField(blank=True)

  access_token = models.CharField(max_length=103, unique=True, null=True)
  expires = models.IntegerField(null=True)
  uid = models.BigIntegerField(unique=True, null=True)

  objects = UserManager()

  class Meta:
    unique_together = (('username', 'uid'), ('access_token', 'expires'))

  USERNAME_FIELD = 'username'

  def facebook_authenticate(self, profile, token):
    self.set_unusable_password()
    self.email = profile['email']
    self.username = profile['username']
    self.first_name = profile['first_name']
    self.last_name = profile['last_name']
    self.save()

    self.uid = profile['id']
    self.save()

    user = authenticate(access_token=token)
    return user
