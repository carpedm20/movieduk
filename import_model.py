from django.core.management import setup_environ
from movieduk import settings
setup_environ(settings)

from django.core import serializers
import json
from core.models import Movie, Actor, SubCharacter, Director, Character
import json

"""
def save_data(fname):
  r=open(fname,'r').read()
  j=json.loads(r)

  for deserialized_object in serializers.deserialize("json", r):
    deserialized_object.save()

fnames=['actors_sub.json','directors.json']#,'actors.json']

for fname in fnames:
  save_data(fname)
"""

f=open('movie_detail.json')
r=f.read()
j=json.loads(r) # directors, actors model import complete!!
j=j[39893:]

print "=======================================================>"

for i in j:
  a = i

  m = Movie()
  keys = ['detail_url','poster_url','title1','title2','story1','story2','country','country_code','time','runtime','year','genre','open','form','grade','index']
  m.detail_url = a['detail_url']

  url = a['detail_url']
  code = url[url.find('code=')+5:]

  ms = Movie.objects.filter(code=code)
  if len(ms) > 0:
    continue

  if code.isdigit():
    m.code = code
  else:
    m.code = -1


  m.poster_url = a['poster_url']
  m.title1 = a['title1']
  m.title2 = a['title2']
  m.story1 = a['story1']
  m.story2 = a['story2']
  m.country = a['country']
  m.country_code = a['country_code']
  m.time = a['time']
  #m.runtime = a['runtime']
  m.year = a['year']
  m.genre = a['genre']
  m.open = a['open']
  #m.form = a['form']
  m.grade = a['grade']
  #m.index = a['index']
  m.save()

  print " > " + a['title1'] + " : " + a['title2']

  actors = i['actors']
  subActors = i['subActors']
  directors = i['director']

  for a in actors:
    c = Character()
    c.part = a['part']
    c.character = a['character']

    if a['profile_url'] != '':
      ob = Actor.objects.get(profile_url=a['profile_url'])
      print ob
      c.actor = ob
      c.save()
      m.main.add(c) 
    else:
      ob = Actor.objects.filter(name=a['name']).filter(en_name=a['en_name']).filter(thumb_url=a['thumb_url']).filter(career1_title=a['career1_title'])
      print ob

      if len(ob) != 1:
        print " ===>>> ERROR"
      else:
        c.actor = ob[0]
        c.save()
        m.main.add(c)

  for s in subActors:
    a = SubCharacter()
    a.character = s['character']

    if s['profile_url'] != '':
      print "Sub profile url : " + s['profile_url']
      try:
        ob = Actor.objects.get(profile_url=s['profile_url'])
      except:
        ob = Actor.objects.filter(name=s['name'])
        if len(ob) != 1:
          print str(len(ob)) + " ERRRRRRRRRRRR: " + s['name']
        else:
          ob=ob[0]
      a.actor = ob
      
    a.save()
    m.sub.add(a)
    
  for d in directors:
    ob = Director.objects.get(profile_url=d['profile_url'])
    m.directors.add(ob)

