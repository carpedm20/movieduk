import json
import os

l = []
dirs = os.listdir('./')
for d in dirs:
    if d.find('.json') != -1 and d.find('naver') == -1 and d.find('django') == -1:
        l.append(d)

j = {}

print l[0]
f = open(l[0],'r')
r = f.read()
f.close()
j[l[0]]=json.loads(r)

k=j[l[0]]
print " > " + l[0] + " : " + str(len(j[l[0]])) + " = " + str(len(k))

for d in l[1:]:
    print d
    f = open(d,'r')
    r = f.read()
    f.close()
    j[d]=json.loads(r)
    k += j[d]
    print " > " + d + " : " + str(len(j[d])) + " = " + str(len(k))

print
print " > " + d + " : " + str(len(k))
f = open('naver_TOTAL.json','w')
json.dump(k,f)
f.close()

