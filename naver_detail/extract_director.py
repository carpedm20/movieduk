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
f.close()
r=f.read()
j=json.loads(r)
len(j)

l=[]
ll=[]
profile_urls = []

for i in j:
  ds = i['director']
  for d in ds:
    url = d['profile_url']
    code = url[url.find('code=')+5:]

    if code.isdigit():
      d['code'] = int(code)
    else:
      d['code'] = -1

    if d['profile_url'] == '':
      same_exist = False
      if d not in l:
        l.append(d)
    else:
      if d['profile_url'] not in profile_urls:
        l.append(d)
        profile_urls.append(d['profile_url'])

for i in l:
  if i['profile_url'] == '':
    print i['name']
    print i['en_name']

count = 1
keys=['profile_url','thumb_url','name','en_name','code']
for i in l:
  k = i.copy()
  #k.update({'index': count})
  i.update({'fields':k, 'model':'core.Director', 'pk':count})

  for k in keys:
    i.pop(k)

  count +=1

k = dumps(l,cls=PythonObjectEncoder)
f=open('directors.json','w')
#json.dump(f,j)
f.write(k)
f.close()
