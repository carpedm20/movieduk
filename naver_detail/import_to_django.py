import json
import sys
import os

l = os.listdir('./')
new_l = []

for i in l:
 if i.find('.json') != -1:
  if i.find('movie') == -1:
    if i.find('django') == -1:
     new_l.append(i)

for f_name in new_l:
  f=open(f_name,'r')

  print "===================="
  print f_name
  print "===================="

  r=f.read()
  j=json.loads(r)

  count = 1
  for i in j:
    k = i.copy()
    k.update({'index': count})
    i.update({'fields':k, 'model':'core.Movie', 'pk':count})

    pop_list = [u'story2', u'story1', u'country', u'time', u'poster_url', u'director', u'title1', u'title2', u'actors', u'country_code', u'year', u'genre', u'open', u'subActors']

    for p in pop_list:
      i.pop(p)
    count += 1

  f.close()

  f=open(f_name.replace('.','_')+'_for_django.json','w')
  json.dump(j,f)
  f.close()
