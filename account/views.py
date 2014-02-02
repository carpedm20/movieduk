# Create your views here.

from django.conf import settings

from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse

from django.contrib.auth import get_user_model
from django.contrib.auth import logout

from django.conf import settings
from django.contrib.auth import models as auth_models

from account import models

import urllib, urllib2
import cgi

#from django.core.context_processros import csrf
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

# Just for simple login
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

import sys

from account.models import *
from UserMovie.models import *
from core.models import *

from django.contrib.auth import get_user_model
User = get_user_model()

import datetime

def profile(request):
  try:
    username = request.session['DukUser']
    user = DukUser.objects.get(username = username)
    ui = user.usermovie_set.all()[0]

    like = ui.liked.all()
    dislike = ui.disliked.all()
    actor_like = ui.actor_liked.all()
    actor_dislike = ui.actor_disliked.all()

    for movie_list in [like, dislike]:
      for m in movie_list:
        m.director_list = m.directors.all()
        m.main_list = m.main.all()[:1]

    for actor_list in [actor_like, actor_dislike]:
      for actor in actor_list:
        actor_movies = Movie.objects.filter(main__actor__code = actor.code).order_by('-rank','-year')
        am_list = []
        for am in actor_movies:
          if am.poster_url != '':
            am_list.append({'poster_url':am.poster_url,'title1':am.title1,'code':am.code})
          if len(am_list) == 8:
            break
        if len(am_list) == 0:
          am_list = False

        actor.am_list = am_list 

    context = {"user":user, "like":like, "dislike":dislike, "actor_like":actor_like, "actor_dislike":actor_dislike}

    return render_to_response('account/profile.html', context)

  except:
    for e in sys.exc_info():
      print e
    return HttpResponseRedirect('/')

def check_movie(request):
  try:
    username = request.session['DukUser']
    user = DukUser.objects.get(username = username)
    ui = user.usermovie_set.all()[0]

    if request.is_ajax() and request.method == "GET":
      code = request.GET.get('code')
      func = request.GET.get('func')

      if func == "like":
        ui = ui.liked
        m = Movie.objects.get(code = code)
      elif func == "dislike":
        ui = ui.disliked
        m = Movie.objects.get(code = code)
      elif func == "actor_like":
        ui = ui.actor_liked
        m = Actor.objects.get(code = code)
      elif func == "actor_dislike":
        ui = ui.actor_disliked
        m = Actor.objects.get(code = code)

      if m in ui.all():
        ui.remove(m)
        data = "[" + str(func) + "] remove success : " + str(m)
      else:
        ui.add(m)
        data = "[" + str(func) + "] add success : " + str(m)
      #print ui.all()

    else:
      data = "fail"
  except:
    for e in sys.exc_info():
      print e
    data = "fail"

  print data
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

@csrf_exempt
def sign_in(request):
  title = 'login'
  error = None

  # Just for simple login
  username = password = ''
  context = RequestContext(request)

  try:
    if request.session['DukUser']:
      return HttpResponseRedirect('/')
  except:
    z = 123

  if request.POST:
    username = request.POST['username']
    password = request.POST['password']
    try:
      user = DukUser.objects.get(username=username, password=password)
      request.session['DukUser'] = user.username

      return HttpResponseRedirect('/')
    except:
      try:
        user = DukUser.objects.get(username=username)
        context['message'] = "Wrong password!"
        return render_to_response('account/login.html', context)
      except:
        user = DukUser.objects.create(username=username,first_name='',last_name='',email='',last_login=datetime.datetime.now(),password=password)
        ui = UserMovie()
        user.usermovie_set.add(ui)
        user.save()
        request.session['DukUser'] = user.username
        return HttpResponseRedirect('/')

  try:
    if user is not None:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect('/')
  except:
    for e in sys.exc_info():
      print e
    sign_out(request)

  return render_to_response('account/login.html', context)

  if request.user.is_authenticated():
    return HttpResponseRedirect('/')

  # I DON'T KNOW!!!
  """
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
      r = urllib.urlopen(url).read()
      response = cgi.parse_qs(r)

      print url
      print r

      access_token = response['access_token'][0]
      expires = response['expires'][0]

      facebook_session = DukUser.objects.get_or_create(access_token=access_token,)[0]
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
  """
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
  try:
    del request.session['DukUser']
  except:
    z=123
  #logout(request.user)
  return HttpResponseRedirect('/')
