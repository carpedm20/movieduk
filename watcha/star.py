import urllib, urllib2


def make_star(mid):
    print "[$] START GET"
    url = 'http://watcha.net/eval/movie/'+mid+'/5'

    headers = { 'POST' : '/eval/movie/'+mid+'/5',
        'HOST' : 'watcha.net',
        'Proxy-Connection': 'keep-alive',
        'Accept' : '*/*',
        'Origin' : 'http://watcha.net',
        'X-CSRF-Token' : 'dXCrywYzygNEprIt0cAatxsZ74myNzJa+8y1nRPROlY=',
        'User-Agent' : 'from.carpedm10.Hi',
        'X-Requested-With' : 'XMLHttpRequest',
        'Referer': 'http://watcha.net/home',
        'Cookie' : '__uvt=; fbm_126765124079533=base_domain=.watcha.net; autologin_auth_key=---+%0A%3Aid%3A+398608%0A%3Atoken%3A+%246%24MsNGylFY%24trORVbHvy8nr.okaQQk2S0A8DOqrMeUqo7nGN9jKow8U.eNYxZrg6gYgE05.o.l4h1AUxQXhGsFGw.HrzssWL%2F%0A; _guinness_session=BAh7C0kiD3Nlc3Npb25faWQGOgZFRkkiJTU1YmI3YmU3MTFiODgwNGI3ZTI2NmUyZmVjNzYyYjZmBjsAVEkiCnNwbGl0BjsARnsGSSIbMjAxMzExMjZfaW50cm9fcmVuZXdhbAY7AFRJIgxyZW5ld2FsBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWRYQ3J5d1l6eWdORXBySXQwY0FhdHhzWjc0bXlOekphKzh5MW5SUFJPbFk9BjsARkkiDHVzZXJfaWQGOwBGaQMQFQZJIhFhYl90ZXN0X2hhc2gGOwBGewBJIgtldmVudHMGOwBGewA%3D--325076de826077434c3d369949d1ca45e52d6849; request_method=GET; uvts=uBfuwjbj7v3SSr2; fbsr_126765124079533=_5Tfj9Txg02pNNxEN9YTFh0L1EMbQPeh2UPwMFLhiGE.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUNCck9RcURWcmVXeS1JcTFidDFJMi1lYjlaQlV5aXBSSENKbU5OUFR6RjNKckp6UFRxbzd2SWRycDd4RHp5c2F1Z0ZEc3lPMGVRMUFreXB2MHZqem0teUtkRWtPc1dnNGxEZ19DX1NXek1oR1J2SDU2dUVHNEo3eWRyMklLN0JKT0t2cWhpdm9PdXpaenhBSWc3cWVnQWpRcHg1ZVIzZGRkQVRWbjdQQXhTdmRMS0x1QWJlX2dqQ0w5TzdyNXRBZ3JWZnZ1RmU3OWptYXNoTVRSNFREbkt6VVJaVFRLcmZGQUZ4MThweE16RmxOZkJzQ3NzM0xDREdEcHZhdnNFcFNVQUVrQVR4QjR3QU44ZGV5N2ZoVUVwOVNDN2xlU0ZYWGpKRjE4TmxicDlKUVdoeFRoZ1U4R3V5MUVSTjJmcjlTRjExSDJJUmdreEJob3drN19JMWdndyIsImlzc3VlZF9hdCI6MTM4NTk5ODM2NCwidXNlcl9pZCI6IjEwMDAwMjA4NjAyNzc0MCJ9; __utma=59143211.498469464.1385783700.1385783700.1385997966.2; __utmb=59143211.122.9.1385998374694; __utmc=59143211; __utmz=59143211.1385783700.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=%EA%B7%B8%EB%A0%87%EA%B2%8C%20%EC%95%84%EB%B2%84%EC%A7%80%EA%B0%80%20%EB%90%9C%EB%8B%A4; __utmv=59143211.|1=Member%20Type=member=1^2=Join%20year%2Fmonth=2013%2F11=1^3=Join%20day=19=1^4=Member%20Id=igkP6JZ5QfyP=1^5=Ip=221.161.111.25=1',
        'Accept-Encoding' : 'sdch',
        'Accept-Language' : 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
        'Content-Length' : '0' }

    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request)
    r = response.read()
    print r

start = 47845
start = 48157
start = 49200

import json
j=json.loads(open('watcha_total.json','r').read())
j.reverse()
j=j[start:]
import thread
import time
for index,i in enumerate(j):
  print " ["+str(start + index)+"] id : " + i['id'] + " : " + i['title']
  #thread.start_new_thread(make_star,(i['id'],))

  make_star(i['id'])
