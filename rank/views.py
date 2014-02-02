# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

from core.forms import CoreListForm, CoreForm
from core.models import Movie, Director, Actor

from django.http import HttpResponse

import json

session_table = {}

MOVIE_COUNT = 5
RANK_COUNT = 100

def index(request):
  global session_table
  if not request.session.get('has_session'):
    request.session['has_session'] = True

  #print "Session : " + str(request.session.session_key)

  # greater than
  actors = Actor.objects.filter(career1_year__gte = '2007').exclude(thumb_url = '').order_by('?')[:2]

  if request.method == 'POST':
    winner = request.Post['winner'].lower()
    winner.rank += 1

  for actor in actors:
    actor.movies = Movie.objects.filter(main__actor__code = int(actor.code)).exclude(poster_url = '')[:MOVIE_COUNT]
    actor.thumb_url = actor.thumb_url[actor.thumb_url.index('&q=')+3:]

  session_table[request.session.session_key] = actors

  rank = Actor.objects.order_by('-rank','-created_on')[:RANK_COUNT]

  context = {'actor1':actors[0], 'actor2':actors[1], 'rank':rank}
  return render_to_response('rank/index.html', context, RequestContext(request))

def get_rank(request):
  global session_table

  if request.is_ajax():
    value = request.GET.get('value', 'left')
    print "value : " + value

    results = []

    if session_table[request.session.session_key]:
      if value == "left":
        session_table[request.session.session_key][0].rank += 1
        session_table[request.session.session_key][0].save()
      elif value == "right":
        session_table[request.session.session_key][1].rank += 1
        session_table[request.session.session_key][1].save()

    actors = Actor.objects.filter(career1_year__gte = '2007').exclude(thumb_url = '').order_by('?')[:2]

    session_table[request.session.session_key] = actors

    for actor in actors:
      actor.movies = Movie.objects.filter(main__actor__code = int(actor.code)).exclude(poster_url = '').order_by('-rank','-year')[:MOVIE_COUNT]
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

    rank = Actor.objects.order_by('-rank','-created_on')[:RANK_COUNT]

    for index, r in enumerate(rank):
      r_json = {}
      r_json['name'] = r.name
      r_json['code'] = r.code
      results.append(r_json)

    data = json.dumps(results)

  else:
    data = 'fail'

  mimetype = 'application/json'
  return HttpResponse(data, mimetype)
  #return HttpResponse(simplejson.dumps( [movie.field for movie in movies]))
