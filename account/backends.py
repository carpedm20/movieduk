from django.conf import settings
from django.contrib.auth import get_user_model
from social.backends.oauth import BaseOAuth2

User = get_user_model()

import cgi
import urllib
#import simplejson

class FacebookBackend(BaseOAuth2):
    name = 'facebook'
    RESPONSE_TYPE = None
    SCOPE_SEPARATOR = ','
    AUTHORIZATION_URL = 'https://www.facebook.com/dialog/oauth'
    ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'
    REVOKE_TOKEN_URL = 'https://graph.facebook.com/{uid}/permissions'
    REVOKE_TOKEN_METHOD = 'DELETE'
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires')
    ]

    def authenticate(self, token=None, *argvs, **kargvs):
        print argvs
        print kargvs

        key, secret = self.get_key_and_secret()
        print "[1]" + key
        url = self.ACCESS_TOKEN_URL
        response = self.get_querystring(url, params={
            'client_id': key,
            'redirect_uri': self.get_redirect_uri(state),
            'client_secret': secret,
            'code': self.data['code']
        })

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
