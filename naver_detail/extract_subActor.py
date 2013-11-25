from json import dumps, loads, JSONEncoder, JSONDecoder
import json
import pickle

class PythonObjectEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
      return JSONEncoder.default(self, obj)
    return {'_python_object': pickle.dumps(obj)}

f=open('movie_detail_for_django.json','r')
r=f.read()
j=json.loads(r)
len(j)

l=[]
ll=[]
profile_urls = []

for i in j:
  ds = i['subActor']
  for d in ds:
    if d['profile_url'] == '':
      same_exist = False
      for lll in ll:
        if lll == d:
          same_exist = True
          break
      if same_exist == True:
        l.append(d)
      else:
        ll.append(d)
    else:
      if d['profile_url'] not in profile_urls:
        l.append(d)
        profile_urls.append(d['profile_url'])

count = 1
keys=['profile_url','name','character']

for i in l:
  k = i.copy()
  #k.update({'index': count})
  i.update({'fields':k, 'model':'core.SubActor', 'pk':count})

  for k in keys:
    i.pop(k)

  count +=1

k = dumps(l,cls=PythonObjectEncoder)
f=open('subActors.json','w')
#json.dump(f,j)
f.write(k)
f.close()
