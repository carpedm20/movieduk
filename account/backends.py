from django.contrib.auth.backends import RemoteUserBackend

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

import cgi
import urllib
#import simplejson

class FacebookBackend(RemoteUserBackend):
    def authenticate(self, token=None):
        facebook_session = User.objects.get(
            access_token=token,
        )
        
        profile = facebook_session.query('me')
        try:
            user = User.objects.get(username=profile['id'])
        except auth_models.User.DoesNotExist, e:
            user = User(username=profile['id'])
        
        user.set_unusable_password()
        user.email = profile['email']
        user.first_name = profile['first_name']
        user.last_name = profile['last_name']
        user.save()

        try:
            User.objects.get(uid=profile['id']).delete()
        except User.DoesNotExist, e:
            pass

        facebook_session.uid = profile['id']
        facebook_session.user = user
        facebook_session.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
