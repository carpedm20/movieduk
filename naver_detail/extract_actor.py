from json import dumps, loads, JSONEncoder, JSONDecoder
import json
import pickle

class PythonObjectEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
      return JSONEncoder.default(self, obj)
    return {'_python_object': pickle.dumps(obj)}

#f=open('movie_detail_for_django.json','r')
f=open('movie_detail.json','r')
#f=open('movie_test.josn','r')
r=f.read()
f.close()
j=json.loads(r)
len(j)
#j=j[:20]

l=[]
ll=[]
profile_urls = []

for i in j:
  acs = i['actors']
  for d in acs:
    url = d['profile_url']
    code = url[url.find('code=')+5:]

    if code.isdigit():
      d[u'code'] = int(code)
    else:
      d[u'code'] = -1

    d.pop('part')
    d.pop('character')

    if d['profile_url'] == '':
      same_exist = False
      if d not in l:
        l.append(d)
    else:
      if d['profile_url'] not in profile_urls:
        l.append(d)
        profile_urls.append(d['profile_url'])
  subs = i['subActors']
  for d in subs:
    url = d['profile_url']
    code = url[url.find('code=')+5:]

    if code.isdigit():
      d[u'code'] = int(code)
    else:
      d[u'code'] = -1

    d.pop('character')

    if d['profile_url'] == '':
      same_exist = False
      if d not in l:
        for k in [u'thumb_url',u'en_name',u'career1_title',u'career1_year',u'career2_title',u'career2_year']:
          d[k] = u''
        l.append(d)
    else:
      if d['profile_url'] not in profile_urls:
        for k in [u'thumb_url',u'en_name',u'career1_title',u'career1_year',u'career2_title',u'career2_year']:
          d[k] = u''
        l.append(d)
        profile_urls.append(d['profile_url'])

count = 1
keys=['profile_url','code','thumb_url','name','en_name','career1_title','career1_year','career2_title','career2_year',]

for i in l:
  k = i.copy()
  #k.update({'index': count})
  i.update({'fields':k, 'model':'core.Actor', 'pk':count})
  count +=1

  for k in keys:
    i.pop(k)

k = dumps(l,cls=PythonObjectEncoder)
f=open('actors_sub.json','w')
#json.dump(f,j)
f.write(k)
f.close()
