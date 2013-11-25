import json
import sys
import os

l = os.listdir('./')
new_l = []

for i in l:
 if i.find('.json') != -1:
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
    #i.pop('actor')
    #i.pop('company')
    #i.pop('director')
    i.pop('title')
    i.pop('url')
    i.pop('year')
    i.pop('open1')
    i.pop('open2')
    i.pop('country')
    i.pop('genre')
    i.pop('form')
    i.pop('grade')
    count += 1

  f.close()

  f=open(f_name.replace('.','_')+'_for_django.json','w')
  json.dump(j,f)
  f.close()
