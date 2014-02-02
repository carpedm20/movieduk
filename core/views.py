#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

from core.forms import CoreListForm, CoreForm
from core.models import Movie, Director, Actor

from django.http import HttpResponse

#from account import settings
from md5 import md5
import json

from django.template import Context, Template
from django.conf import settings

import urllib

from account.models import *

# youtube
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyDsEDIEMlR1A8ATswD9R7BpOeeDgxMJ6tU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

def youtube_search(query):
  global youtube

  search_response = youtube.search().list(
    q=query,
    part="id,snippet",
    maxResults=3,
  ).execute()

  img_list = []
  id_list = [] # http://www.youtube.com/embed/LmkWh4ryih0

  for i in search_response.get("items", []):
    #img_list.append(i['snippet']['thumbnails']['default']['url'])
    img_list.append(i['snippet']['thumbnails']['medium']['url'])
    id_list.append(i['id']['videoId'])

  return id_list, img_list

# csrf
from django.views.decorators.csrf import csrf_exempt

PER_PAGE = 30
MEDIA_URL = 'http://hexa.perl.sh/~carpedm30/img/'

def make_index_context(request, short=False):
  if not request.session.get('has_session'):
    request.session['has_session'] = True

  title = "hello world!"

  M = Movie.objects.exclude(year='xxxx')

  #if request.method == 'POST':
  if True:
    #try:
    #  query = request.POST.get('query')
    #except:
    #  query = ""
    genres = request.COOKIES.get('genres')
    nations = request.COOKIES.get('nations')
    years = request.COOKIES.get('years')

    try:
      genres = urllib.unquote(genres).decode('utf8')
    except:
      genres = "all"

    try:
      nations = urllib.unquote(nations).decode('utf8')
    except:
      nations = "all"

    try:
      years = urllib.unquote(years).decode('utf8')
    except:
      years = "all"

    #if query != None:
    #  movies = M.filter(title1__contains = query)

    if genres != 'all' and genres != None and genres != "":
      genres = genres.split(',')
      for g in genres:
        #print g
        try:
          movies |= M.filter(genre__contains = num_to_genre(g))
        except:
          movies = M.filter(genre__contains = num_to_genre(g))

    if nations != 'all' and nations != None and nations != "":
      nations = nations.split(',')
      name = [num_to_nation(n) for n in nations]

      exclude_list = ["한국","미국","일본","중국"]

      if name == 'x':
        try:
          movies |= movies.exclude(country__in = exclude_list)
        except:
          movies = M.exclude(country__in = exclude_list)
      else:
        try:
          movies = movies.filter(country__in = name)
          #movies |= M.filter(country__contains = name)
        except:
          movies = M.filter(country__in = name)

    if years != 'all' and years != None and years != "":
      #print years
      years = years.split(',')
      year_list = []
      for y in years:
        y_start, y_end = y.split('~')
        year_list_int = range(int(y_start), int(y_end) + 1)
        year_list += [str(y) for y in year_list_int]

      try:
        movies = movies.filter(year__in = year_list)
        #movies |= M.filter(year__in = year_list)
      except:
        movies = M.filter(year__in = year_list)
  else:
    movies = Movie.objects.exclude(year='xxxx')

  try:
    movies = movies.order_by('-rank','-year')[:10]
  except:
     movies = Movie.objects.exclude(year='xxxx').order_by('-rank','-year')[:10]

  try:
    username = request.session['DukUser']
    user = DukUser.objects.get(username = username)
    ui = user.usermovie_set.all()[0]
  except:
    user = None

  for m in movies:
    m.director_list = m.directors.all()
    m.main_list = m.main.all()

    if m.poster_url != '':
      #print " =====================> " + m.poster_url
      url = m.poster_url
      new_url = url[url.rfind('naver.net') + 10:]
      m.poster = m.year + '/' + m.country_code + '/' + 'pic_' + md5(new_url).hexdigest() + '.jpg'
    else:
      m.poster = ''

    if m.poster_url == '':
      m.poster_url = False

    m.like_count = len(DukUser.objects.filter(usermovie__liked = m))
    m.dislike_count = len(DukUser.objects.filter(usermovie__disliked = m))

    if user:
      if m in ui.liked.all():
        m.like = True
      else:
        m.like = False

      if m in ui.disliked.all():
        m.dislike = True
      else:
        m.dislike = False

  context = {'MEDIA_URL': MEDIA_URL, 'movies' : movies, 'title': title, 'infinite': "true"}
  return context

def random(request):
  random_movie = Movie.objects.exclude(poster_url='').order_by('?')[:300]

  context = {"random_movie":random_movie}

  return render_to_response('core/random.html', context, RequestContext(request))

@csrf_exempt
def index(request):
  context = make_index_context(request)
  context['settings'] = settings
  return render_to_response('core/index_infinite.html', context, RequestContext(request))

@csrf_exempt
def index_short(request):
  context = make_index_context(request)
  context['settings'] = settings
  return render_to_response('core/index_short.html', context, RequestContext(request))

@csrf_exempt
def num_to_genre(num):
  # for watcha
  if num == '35':
    return '범죄'
  elif num == '36':
    return '드라마'
  elif num == '37':
    return '코미디'
  elif num == '38':
    return '멜로/애정/로맨스'
  elif num == '39':
    return '스릴러'
  elif num == '40':
    return '가족'
  elif num == '41':
    return '전쟁'
  #################
  elif num == '44':
    return '판타지'
  elif num == '45':
    return '액션'
  elif num == '46':
    return 'SF'
  elif num == '47':
    return '애니메이션'
  elif num == '46':
    return '공포'
  # below is for naver
  elif num == '47':
    return '미스터리'
  elif num == '48':
    return '모험'

@csrf_exempt
def num_to_nation(num):
  if num == '1':
    return '한국'
  elif num == '2':
    return '미국'
  elif num == '3':
    return '일본'
  elif num == '4':
    return '중국'
  #elif num == '5':
    #return '유럽'
  elif num == '6':
    return 'x'
 
@csrf_exempt
def movie_filter(request):
  #print request.POST

  genres = request.POST.get('genres')
  nations = request.POST.get('nations')
  years = request.POST.get('years')

  M = Movie.objects.all().exclude(year='xxxx')

  if genres != 'all':
    genres = genres.split(',')
    for g in genres:
      #genres_str.append(num_to_genre(g))
      #print num_to_genre(g)
      try:
        movies |= M.filter(genre__contains = num_to_genre(g))
      except:
        movies = M.filter(genre__contains = num_to_genre(g))
    
  if nations != 'all':
    #print nations
    nations = nations.split(',')
    for n in nations:
      name = num_to_nation(n)
      exclude_list = ["한국","미국","일본","중국"]

      if name == 'x':
        try:
          movies = movies.exclude(country__in = exclude_list)
        except:
          movies = M.exclude(country__in = exclude_list)
      else:
        try:
          movies = movies.filter(country = name)
          #movies |= M.filter(country__contains = name)
        except:
          movies = M.filter(country = name)

  if years != 'all':
    #print years
    years = years.split(',')
    year_list = []
    for y in years:
      y_start, y_end = y.split('~')
      year_list_int = range(int(y_start), int(y_end) + 1)
      year_list += [str(y) for y in year_list_int]
      
    try:
      movies |= M.filter(year__in = year_list)
    except:
      movies = M.filter(year__in = year_list)

  context = {'movies' : movies.order_by('-rank','-year')[:10], }
  return render_to_response('core/index_infinite.html', context, RequestContext(request))

# http://10.20.16.52:8000/search/movie/title?query=e
def movie_search(request, option = "title"):
  title = "SEARCH"
  query = request.GET.get('query')

  M = Movie.objects.all().exclude(year='xxxx')

  try:
    username = request.session['DukUser']
    user = DukUser.objects.get(username = username)
    ui = user.usermovie_set.all()[0]
  except:
    user = None

  if option == 'title':
    movies = M.filter(title1__contains=query).order_by('-rank','-year')[:10]
  elif option == 'year':
    movies = M.filter(year=query).order_by('-rank','-year')[:10]
  elif option == 'genre':
    movies = M.filter(genre=query).order_by('-rank','-year')[:10]
  elif option == 'country':
    movies = M.filter(country=query).order_by('-rank','-year')[:10]
  else:
    movies = []

  for m in movies:
    m.director_list = m.directors.all()
    m.main_list = m.main.all()

    m.like_count = len(DukUser.objects.filter(usermovie__liked = m))
    m.dislike_count = len(DukUser.objects.filter(usermovie__disliked = m))

    if user:
      if m in ui.liked.all():
        m.like= True
      else:
        m.like = False

      if m in ui.disliked.all():
        m.dislike = True
      else:
        m.dislike = False

    if m.poster_url != '':
      #print " =====================> " + m.poster_url
      url = m.poster_url
      new_url = url[url.rfind('naver.net') + 9:]
      m.poster = m.year + '/' + m.country_code + '/' + 'pic_' + md5(new_url).hexdigest() + '.jpg'
    else:
      m.poster = ''

    if m.poster_url == '':
      m.poster_url = False

  if len(movies) < 10:
    end = True
  else:
    end = False

  context = {'movies' : movies, 'title': title, 'end': end}
  return render_to_response('core/index_search_infinite.html', context, RequestContext(request))

# http://10.20.16.52:8000/info/director/2639
def director_info(request, code):
  title = "DIRECTOR PROFILE"

  try:
    username = request.session['DukUser']
    user = DukUser.objects.get(username = username)
    ui = user.usermovie_set.all()[0]
  except:
    user = None

  director = Director.objects.get(code = int(code))
  movies = Movie.objects.filter(directors = director).order_by('-rank','-year')

  director.like_count = len(DukUser.objects.filter(usermovie__director_liked = director))
  director.dislike_count = len(DukUser.objects.filter(usermovie__director_disliked = director))

  if user:
    if director in ui.director_liked.all():
      director.like= True
    else:
      director.like = False

    if director in ui.director_disliked.all():
      director.dislike = True
    else:
      director.dislike = False

  if director.thumb_url == "":
    director.thumb_url = False

  for m in movies:
    m.like_count = len(DukUser.objects.filter(usermovie__liked = m))
    m.dislike_count = len(DukUser.objects.filter(usermovie__liked = m))

    if user:
      if m in ui.liked.all():
        m.like = True
      else:
        m.like = False

      if m in ui.disliked.all():
        m.dislike = True
      else:
        m.dislike = False

    m.director_list = m.directors.all()
    m.main_list = m.main.all()

    if m.poster_url != '':
      print " =====================> " + m.poster_url
      url = m.poster_url
      new_url = url[url.rfind('naver.net') + 9:]
      m.poster = m.year + '/' + m.country_code + '/' + 'pic_' + md5(new_url).hexdigest() + '.jpg'
    else:
      m.poster = ''

    if m.poster_url == '':
      m.poster_url = False

  context = {'director' : director, 'movies' : movies, 'title': title}
  return render_to_response('core/director.html', context, RequestContext(request))

# http://10.20.16.52:8000/info/actor/15330
def actor_info(request, code):
  title = "Actor PROFILE"

  try:
    username = request.session['DukUser']
    user = DukUser.objects.get(username = username)
    ui = user.usermovie_set.all()[0]
  except:
    user = None

  actor = Actor.objects.get(code = int(code))
  actor.rank += 1
  actor.save()
  #print actor.rank

  actor.like_count = len(DukUser.objects.filter(usermovie__actor_liked = actor))
  actor.dislike_count = len(DukUser.objects.filter(usermovie__actor_disliked = actor))

  if user:
    if actor in ui.actor_liked.all():
      actor.like= True
    else:
      actor.like = False

    if actor in ui.actor_disliked.all():
      actor.dislike = True
    else:
      actor.dislike = False

  movies = Movie.objects.filter(main__actor__code = int(code)).order_by('-rank','-year')

  if actor.thumb_url == "":
    actor.thumb_url = False

  for m in movies:
    m.like_count = len(DukUser.objects.filter(usermovie__liked = m))
    m.dislike_count = len(DukUser.objects.filter(usermovie__disliked = m))

    m.director_list = m.directors.all()
    m.main_list = m.main.all()

    if user:
      if m in ui.liked.all():
        m.like = True
      else:
        m.like = False

      if m in ui.disliked.all():
        m.dislike = True
      else:
        m.dislike = False

    if m.poster_url != '':
      url = m.poster_url
      new_url = url[url.rfind('naver.net') + 9:]
      m.poster = m.year + '/' + m.country_code + '/' + 'pic_' + md5(new_url).hexdigest() + '.jpg'
    else:
      m.poster = ''

    if m.poster_url == '':
      m.poster_url = False

  context = {'actor' : actor, 'movies' : movies, 'title': title}
  return render_to_response('core/actor.html', context, RequestContext(request))

def movie_info(request, code):
  title = "Movie Info"

  movie = Movie.objects.get(code = int(code))
  movie.rank += 1
  movie.save()
  directors = movie.directors.all()
  mains = movie.main.all()

  try:
    username = request.session['DukUser']
    user = DukUser.objects.get(username = username)
    ui = user.usermovie_set.all()[0]
  except:
    user = None

  for d in directors:
    d.like_count = len(DukUser.objects.filter(usermovie__director_liked = d))
    d.dislike_count = len(DukUser.objects.filter(usermovie__director_disliked = d))

    if user:
      if d in ui.director_liked.all():
        d.like= True
      else:
        d.like = False

      if d in ui.director_disliked.all():
        d.dislike = True
      else:
        d.dislike = False

    director_movies = Movie.objects.filter(directors__code = d.code).order_by('-rank','-year')
    dm_list = []
    for dm in director_movies:
      if dm == movie:
        continue
      if dm.poster_url != '':
        dm_list.append({'poster_url':dm.poster_url,'title1':dm.title1,'code':dm.code})
      if len(dm_list) == 10:
        break
    if len(dm_list) == 0:
      dm_list = False
    d.dm_list = dm_list

  for m in mains:
    # rank up
    ac = m.actor
    #ac.rank += 0.1
    #ac.save()

    ac.like_count = len(DukUser.objects.filter(usermovie__actor_liked = ac))
    ac.dislike_count = len(DukUser.objects.filter(usermovie__actor_disliked = ac))

    if user:
      if ac in ui.actor_liked.all():
        ac.like= True
      else:
        ac.like = False

      if ac in ui.actor_disliked.all():
        ac.dislike = True
      else:
        ac.dislike = False

    # popular movie for actor
    actor_movies = Movie.objects.filter(main__actor__code = m.actor.code).order_by('-rank','-year')
    am_list = []
    for am in actor_movies:
      if am == movie:
        continue
      if am.poster_url != '':
        am_list.append({'poster_url':am.poster_url,'title1':am.title1,'code':am.code})
      if len(am_list) == 9:
        break

    if len(am_list) == 0:
      am_list = False
    m.am_list = am_list

  subs = movie.sub.all()

  if movie.poster_url == "":
    movie.poster_url = False

  # youtube
  try:
    if movie.country != u'한국':
      youtube_query = movie.title2 + " trailer"
    else:
      youtube_query = movie.title1 + " " + movie.year

    print youtube_query
    youtubes, youtube_thumbs = youtube_search(youtube_query)
  except:
    youtubes = False
    youtube_thumbs = False

  if youtubes != False:
    youtube = zip(youtubes, youtube_thumbs)
  else:
    youtube = False

  context = {'movie' : movie, 'youtube' : youtube, 'directors' : directors, 'mains' : mains, 'subs' : subs, 'title': title}
  return render_to_response('core/movie.html', context, RequestContext(request))

# auto complete
def get_info(request):
  print " ^^^^^ GET INFO 1"
  if request.is_ajax():
    q = request.GET.get('term', '')
    results = []

    movies = Movie.objects.filter(title1__icontains = q ).order_by('-rank','-year')[:5]
    for movie in movies:
      movie_json = {}
      movie_json['code'] = str(movie.code)
      movie_json['info'] = "movie"
      #movie_json['director'] = movie.directors.all()[0].name
      #movie_json['code'] = movie.directors.all()[0].code
      movie_json['value'] = movie.title1 + " "  +  movie.year
      results.append(movie_json)

    actors = Actor.objects.filter(name__icontains = q).order_by('-rank')[:5]
    for a in actors:
      a_json = {}
      a_json['code'] = str(a.code)
      a_json['info'] = "actor"
      if a.en_name != "":
        a_json['value'] = a.name + "(" + a.en_name + ")"
      else:
        a_json['value'] = a.name
      results.append(a_json)

    directors = Director.objects.filter(name__icontains = q)[:5]
    for d in directors:
      d_json = {}
      d_json['code'] = str(d.code)
      d_json['info'] = "director"
      d_json['value'] = d.name
      results.append(d_json)

    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)
  #return HttpResponse(simplejson.dumps( [movie.field for movie in movies]))

def make_list(request, short=False):
  if request.is_ajax() and request.method == "POST":
    count = int(request.POST.get('count', '10'))
    page = int(request.POST.get('page', '0'))

    #print "count : " + str(count) + ", page : " + str(page)

    M = Movie.objects.exclude(year='xxxx')

    try:
      query = request.POST.get('query')
    except:
      query = ""

    genres = request.POST.get('genres')
    nations = request.POST.get('nations')
    years = request.POST.get('years')

    if query != None:
      movies = M.filter(title1__contains = query)

    if genres != 'all' and genres != None and genres != "":
      genres = genres.split(',')
      for g in genres:
        try:
          movies |= M.filter(genre__contains = num_to_genre(g))
        except:
          movies = M.filter(genre__contains = num_to_genre(g))
        #print len(movies)

    if nations != 'all' and nations != None and nations != "":
      nations = nations.split(',')
      name = [num_to_nation(n) for n in nations]

      exclude_list = ["한국","미국","일본","중국"]

      if name == 'x':
        try:
          movies |= movies.exclude(country__in = exclude_list)
        except:
          movies = M.exclude(country__in = exclude_list)
      else:
        try:
          movies = movies.filter(country__in = name)
          #movies |= M.filter(country__contains = name)
        except:
          movies = M.filter(country__in = name)

    if years != 'all' and years != None and years != "":
      #print years
      years = years.split(',')
      year_list = []
      for y in years:
        y_start, y_end = y.split('~')
        year_list_int = range(int(y_start), int(y_end) + 1)
        year_list += [str(y) for y in year_list_int]

      try:
        movies = movies.filter(year__in = year_list)
        #movies |= M.filter(year__in = year_list)
      except:
        movies = M.filter(year__in = year_list)

    try:
      movies = movies.order_by('-rank','-year')[page * count:page * count + count]
    except:
      movies = M.order_by('-rank','-year')[page * count:page * count + count]

    movie_json = {}
    if count > len(movies):
      movie_json['end'] = True

    if len(movies) == 0:
      return 'fail'

    if short:
      f = open(settings.TEMPLATE_DIRS[0] + '/core/movie_item_short.html','r')
    else:
      f = open(settings.TEMPLATE_DIRS[0] + '/core/movie_item.html','r')

    r = f.read()
    t = Template(r)

    try:
      username = request.session['DukUser']
      user = DukUser.objects.get(username = username)
      ui = user.usermovie_set.all()[0]
    except:
      user = None

    for m in movies:
      m.director_list = m.directors.all()
      m.main_list = m.main.all()

      m.like_count = len(DukUser.objects.filter(usermovie__liked = m))
      m.dislike_count = len(DukUser.objects.filter(usermovie__disliked = m))

      if m.poster_url != '':
        url = m.poster_url
        new_url = url[url.rfind('naver.net') + 9:]
        m.poster = m.year + '/' + m.country_code + '/' + 'pic_' + md5(new_url).hexdigest() + '.jpg'
      else:
        m.poster = ''

      if m.poster_url == '':
        m.poster_url = False

      if user:
        if m in ui.liked.all():
          m.like = True
        else:
          m.like = False

        if m in ui.disliked.all():
          m.dislike = True
        else:
          m.dislike = False

    context = {'MEDIA_URL': MEDIA_URL, 'movies' : movies}

    html = t.render(Context(context))

    movie_json['source'] = html

    results = []
    results.append(movie_json)

    data = json.dumps(results)
  else:
    data = 'fail'

  return data

@csrf_exempt
def get_list(request):
  print " ^^^^^ GET INFO 2"

  mimetype = 'application/json'
  return HttpResponse(make_list(request, False), mimetype)

@csrf_exempt
def get_search_list(request):
  if request.is_ajax() and request.method == "POST":
    try:
      username = request.session['DukUser']
      user = DukUser.objects.get(username = username)
      ui = user.usermovie_set.all()[0]
    except:
      user = None

    query = request.POST.get('query')
    #print query
    option = request.POST.get('option')
    #print option
    count = int(request.POST.get('count', '10'))
    page = int(request.POST.get('page', '0'))

    M = Movie.objects.all().exclude(year='xxxx')

    if option == 'title':
      movies = M.filter(title1__contains=query).order_by('-rank','-year')
    elif option == 'year':
      movies = M.filter(year=query).order_by('-rank','-year')
    elif option == 'genre':
      movies = M.filter(genre=query).order_by('-rank','-year')
    elif option == 'country':
      movies = M.filter(country=query).order_by('-rank','-year')
    else:
      movies = []

    movies = movies.order_by('-rank','-year')[page * count:page * count + count]

    movie_json = {}
    if count > len(movies):
      movie_json['end'] = True

    if len(movies) == 0:
      return 'fail'

    f = open(settings.TEMPLATE_DIRS[0] + '/core/movie_item.html','r')

    r = f.read()
    t = Template(r)

    for m in movies:
      m.like_count = len(DukUser.objects.filter(usermovie__liked = m))
      m.dislike_count = len(DukUser.objects.filter(usermovie__disliked = m))

      if user:
        if m in ui.liked.all():
          m.like= True
        else:
          m.like = False

        if m in ui.disliked.all():
          m.dislike = True
        else:
          m.dislike = False

      m.director_list = m.directors.all()
      m.main_list = m.main.all()

      if m.poster_url != '':
        url = m.poster_url
        new_url = url[url.rfind('naver.net') + 9:]
        m.poster = m.year + '/' + m.country_code + '/' + 'pic_' + md5(new_url).hexdigest() + '.jpg'
      else:
        m.poster = ''

      if m.poster_url == '':
        m.poster_url = False

    context = {'MEDIA_URL': MEDIA_URL, 'movies' : movies}

    html = t.render(Context(context))

    movie_json['source'] = html

    results = []
    results.append(movie_json)

    data = json.dumps(results)
  else:
    data = "fail"

  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

@csrf_exempt
def get_short_list(request):
  print " ^^^^^ GET INFO 3"

  mimetype = 'application/json'
  return HttpResponse(make_list(request, True), mimetype)
