import json
import sys
import os

l = os.listdir('./')
new_l = []

for i in l:
 if i.find('.json') != -1:
  if i.find('total') == -1:
   if i.find('movie_') == -1:
    new_l.append(i)

count = 0
for f_name in new_l:
  f=open(f_name,'r')
  print "===================="
  print f_name
  print "===================="
  r=f.read()
  j=json.loads(r)
  print " LENGTH : " + str(len(j))
  if count == 0:
   result = j
   count += 1
  else:
   result += j
   print " ==> LENGTH : " + str(len(result))
  f.close()

f = open('watcha_total.json','w')
json.dump(result,f)
f.close()
