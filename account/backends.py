from django.conf import settings
from django.contrib.auth import models as auth_models

import cgi
import urllib
#import simplejson

from account.models import UserProfile, FacebookSession

class FacebookBackend:
  def authenticate(self, token=None):
    facebook_session = FacebookSession.objects.get(access_token=token,)
    profile = facebook_session.query('me')

    print " [#] AUTHENTICATION : username = " + profile['id']
    try:
      # if exist, get existing object
      user = auth_models.User.objects.get(username=profile['id'])
    except auth_models.User.DoesNotExist, e:
      # or make new object
      user = auth_models.User(username=profile['id'])
      user_profile = UserProfile(user=user)

      user.set_unusable_password()
      user.email = profile['email']
      user.name = profile['name'] # u'\ud3ec\ud0c8\ubd07'
      user.first_name = profile['first_name'] # u'\ubd07'
      user.last_name = profile['last_name'] # u'\ud3ec\ud0c8'
      #user.username = profile['username']
      #user.bio = profile['bio']
      #user.gender = profile['gender']
      #user.link = profile['link']
      #user.location = profile['location']
      user.save()

    try:
      # delete existing object
      FacebookSession.objects.get(uid=profile['id']).delete()
    except FacebookSession.DoesNotExist, e:
      pass

    facebook_session.uid = profile['id']
    facebook_session.user = user
    facebook_session.save()

    return user

  def get_user(self, user_id):
    try:
      return auth_models.User.objects.get(pk=user_id)
    except auth_models.User.DoesNotExist:
      return None
