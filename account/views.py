# -*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse

from django.contrib.auth import logout

import cgi
#import simplejson
import urllib

from account import settings, models

#from django.core.context_processros import csrf
from django.contrib.auth.decorators import login_required

def sign_in(request):
    title = 'login'
    error = None

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    
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
                    
                    return HttpResponseRedirect('/')
                else:
                    error = 'AUTH_DISABLED'
            else:
                error = 'AUTH_FAILED'
        elif 'error_reason' in request.GET:
            error = 'AUTH_DENIED'

    template_context = {'settings': settings, 'error': error, 'title' : title}
    print error
    return render_to_response('account/login.html', template_context, context_instance=RequestContext(request))

def sign_up(request):
  title = "sign up"
  if request.user.is_authenticated():
    return HttpResponseRedirect('/')
  else:
    error = 'AUTH_FAILED'
    template_context = {'settings': settings, 'error': error, 'title' : title}
    print error
    return render_to_response('account/join.html', template_context, context_instance=RequestContext(request))

def sign_out(request):
  logout(request)
  return HttpResponseRedirect('/')

"""
#@login_required
def view_profile(request):
  if request.method == 'POST':
    form = UserProfileForm(request.POST, instance=request.user.profile) # original instance of 
    if form.is_vaild(): # cached value
      form.save()
      return HttpResponseRedirect('/')
    else:
      user = request.user
      profile = user.profile
      form = UserProfileForm(instance = profile)

    args = {}
    args.update(csrf(request))
    args['form'] = form

   return render_to_response('account/profile.html', args)
"""
