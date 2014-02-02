from django.db import models
from core.models import *

class CustomUserManager(models.Manager):
  def create_user(self, username, email=None):
    print "==============DUKUSERCREATE"
    return self.model._default_manager.create(username=username, first_name='')

class DukUser(models.Model):
  print "==============DUKUSERCREATE"
  #social_auth requirements
  username = models.CharField(max_length=30)
  first_name = models.CharField(max_length=10, blank=True, null=True)
  last_name = models.CharField(max_length=10, blank=True, null=True)
  password = models.CharField(max_length=30)

  email = models.EmailField(blank=True, null=True)
  last_login = models.DateTimeField(blank=True, null=True)
  is_active = models.BooleanField(default=True)

  #objects = CustomUserManager()

  def __unicode__(self):
    return self.username

  def is_authenticated(self):
    return True
