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

PER_PAGE = 30
MEDIA_URL = 'http://hexa.perl.sh/~carpedm30/img/'

def index(request):
  #if request.user.is_authenticated():
  #  return HttpResponseRedirect('/run/')
  title = "hello world!"
  #movies = Movie.objects.order_by('-year')[:20]
  #movies = Movie.objects.all()
  movies = Movie.objects.order_by('-rank','-year')[:10]
  #movies = movies[len(movies)-10:] 

  for m in movies:
    m.director_list = m.directors.all()
    m.main_list = m.main.all()
    #print " RANK : " + str(m.rank)

    if m.poster_url != '':
      #print " =====================> " + m.poster_url
      url = m.poster_url
      new_url = url[url.rfind('naver.net') + 9:]
      m.poster = m.year + '/' + m.country_code + '/' + 'pic_' + md5(new_url).hexdigest() + '.jpg'
    else:
      m.poster = ''

    if m.poster_url == '':
      m.poster_url = False

  context = {'MEDIA_URL': MEDIA_URL, 'movies' : movies, 'title': title}
  return render_to_response('core/index.html', context, RequestContext(request))

# http://10.20.16.52:8000/search/movie/title?query=e
def movie_search(request, option = "title"):
  title = "SEARCH"
  query = request.GET.get('query')

  if option == 'title':
    movies = Movie.objects.filter(title1__contains=query).order_by('-rank','-year')[:PER_PAGE]
  elif option == 'year':
    movies = Movie.objects.filter(year=query).order_by('-rank','-year')[:PER_PAGE]
  elif option == 'genre':
    movies = Movie.objects.filter(genre=query).order_by('-rank','-year')[:PER_PAGE]
  elif option == 'country':
    movies = Movie.objects.filter(country=query).order_by('-rank','-year')[:PER_PAGE]
  else:
    movies = []

  for m in movies:
    m.director_list = m.directors.all()
    m.main_list = m.main.all()

    if m.poster_url != '':
      #print " =====================> " + m.poster_url
      url = m.poster_url
      new_url = url[url.rfind('naver.net') + 9:]
      m.poster = m.year + '/' + m.country_code + '/' + 'pic_' + md5(new_url).hexdigest() + '.jpg'
    else:
      m.poster = ''

    if m.poster_url == '':
      m.poster_url = False

  context = {'movies' : movies, 'title': title}
  return render_to_response('core/index.html', context, RequestContext(request))

# http://10.20.16.52:8000/info/director/2639
def director_info(request, code):
  title = "DIRECTOR PROFILE"

  director = Director.objects.get(code = int(code))
  movies = Movie.objects.filter(directors = director).order_by('-rank','-year')

  if director.thumb_url == "":
    director.thumb_url = False

  for m in movies:
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

  actor = Actor.objects.get(code = int(code))
  movies = Movie.objects.filter(main__actor__code = int(code)).order_by('-rank','-year')

  if actor.thumb_url == "":
    actor.thumb_url = False

  for m in movies:
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

  context = {'actor' : actor, 'movies' : movies, 'title': title}
  return render_to_response('core/actor.html', context, RequestContext(request))

def movie_info(request, code):
  title = "Movie Info"

  movie = Movie.objects.get(code = int(code))
  movie.rank += 1
  movie.save()
  directors = movie.directors.all()
  mains = movie.main.all()

  for m in mains:
    actor_movies = Movie.objects.filter(main__actor__code = m.actor.code).order_by('-rank','-year')
    am_list = []
    for am in actor_movies:
      if am == movie:
        continue
      if am.poster_url != '':
        am_list.append({'poster_url':am.poster_url,'title1':am.title1,'code':am.code})
      if len(am_list) == 4:
        break
    if len(am_list) == 0:
      am_list = False
    m.am_list = am_list

  subs = movie.sub.all()

  if movie.poster_url == "":
    movie.poster_url = False

  context = {'movie' : movie, 'directors' : directors, 'mains' : mains, 'subs' : subs, 'title': title}
  return render_to_response('core/movie.html', context, RequestContext(request))

def get_info(request):
  print " ^^^^^ GET INFO"
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

    actors = Actor.objects.filter(name__icontains = q)[:5]
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

def get_list(request):
  print " ^^^^^ GET INFO"
  title = "Hello"

  if request.is_ajax():
    count = int(request.GET.get('count', '10'))
    page = int(request.GET.get('page', '0'))
    
    movies = Movie.objects.order_by('-rank','-year')[page * count:page * count + count]

    f = open(settings.TEMPLATE_DIRS[0] + '/core/movie_item.html','r')
    r = f.read()
    t = Template(r)

    for m in movies:
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

    context = {'MEDIA_URL': MEDIA_URL, 'movies' : movies, 'title': title}

    html = t.render(Context(context))

    movie_json = {}
    movie_json['source'] = html

    results = []
    results.append(movie_json)

    data = json.dumps(results)
  else:
    data = 'fail'

  mimetype = 'application/json'
  return HttpResponse(data, mimetype)
