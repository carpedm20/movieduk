# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

from core.forms import CoreListForm, CoreForm
from core.models import Movie, Director, Actor

from django.http import HttpResponse

import json

def index(request):
  # greater than
  actors = Actor.objects.filter(career1_year__gte = '2007').exclude(thumb_url = '').order_by('?')[:2]

  if request.method == 'POST':
    winner = request.Post['winner'].lower()
    winner.rank += 1

  for actor in actors:
    actor.movies = Movie.objects.filter(main__actor__code = int(actor.code)).exclude(poster_url = '')[:5]
    actor.thumb_url = actor.thumb_url[actor.thumb_url.index('&q=')+3:]

  context = {'actor1':actors[0], 'actor2':actors[1] }
  return render_to_response('rank/index.html', context, RequestContext(request))

def get_rank(request):
  if request.is_ajax():
    results = []

    actors = Actor.objects.filter(career1_year__gte = '2007').exclude(thumb_url = '').order_by('?')[:2]

    if request.method == 'POST':
      winner = request.Post['winner'].lower()
      winner.rank += 1

    for actor in actors:
      actor.movies = Movie.objects.filter(main__actor__code = int(actor.code)).exclude(poster_url = '').order_by('-rank','-year')[:6]
      actor.thumb_url = actor.thumb_url[actor.thumb_url.index('&q=')+3:]

      a_json = {}
      a_json['thumb_url'] = actor.thumb_url
      a_json['movies'] = []

      for movie in actor.movies:
        m_json = {}
        m_json['poster_url'] = movie.poster_url
        m_json['code'] = movie.code
        m_json['title1'] = movie.title1
        a_json['movies'].append(m_json)

      a_json['name'] = actor.name
      a_json['en_name'] = actor.en_name
      results.append(a_json)

    data = json.dumps(results)
  else:
    data = 'fail'

  mimetype = 'application/json'
  return HttpResponse(data, mimetype)
  #return HttpResponse(simplejson.dumps( [movie.field for movie in movies]))
