# -*- coding: utf-8 -*-
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

import cgi
#import simplejson
import urllib

from facebook_account import settings, models
def login(request):
    error = None

    if request.user.is_authenticated():
        return HttpResponseRedirect('/run/')
    
    if request.GET:    
        if 'code' in request.GET:        
            args = {
                'client_id': settings.FACEBOOK_APP_ID,
                'redirect_uri': settings.FACEBOOK_REDIRECT_URI,
                'client_secret': settings.FACEBOOK_API_SECRET,
                'code': request.GET['code'],
            }
            url = 'https://graph.facebook.com/oauth/access_token?' + \
                    urllib.urlencode(args)
            response = cgi.parse_qs(urllib.urlopen(url).read())

            access_token = response['access_token'][0]
            expires = response['expires'][0]

            facebook_session = models.FacebookSession.objects.get_or_create(access_token=access_token,)[0]
            facebook_session.expires = expires
            facebook_session.save()
            
            user = auth.authenticate(token=access_token)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    
                    return HttpResponseRedirect('/run/')
                else:
                    error = 'AUTH_DISABLED'
            else:
                error = 'AUTH_FAILED'
        elif 'error_reason' in request.GET:
            error = 'AUTH_DENIED'

    template_context = {'settings': settings, 'error': error}
    print error
    return render_to_response('facebook_account/login.html', template_context, context_instance=RequestContext(request))

def run(request) :
    s = 'hellow'
    return HttpResponse(s)
