import json
f=open('f.json','r')
r=f.read()
j=json.loads(r)

count = 1
for i in j:
    k = i.copy()
    k.update({'index': count})
    i.update({'fields':k, 'model':'core.Movie', 'pk':count})
    i.pop('actor')
    i.pop('company')
    i.pop('director')
    i.pop('genre')
    i.pop('title')
    i.pop('url')
    i.pop('year')
    count += 1

f.close()

f=open('initial_data.json','w')
json.dump(j,f)
f.close()
