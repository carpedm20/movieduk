import urllib, urllib2


def make_star(mid):
    print "[$] START GET"
    url = 'http://watcha.net/eval/movie/'+mid+'/5'

    headers = { 'POST' : '/eval/movie/'+mid+'/5',
        'HOST' : 'watcha.net',
        'Connection' : 'Close',
        'Proxy-Connection': 'keep-alive',
        'Accept' : '*/*',
        'Origin' : 'http://watcha.net',
        'X-CSRF-Token' : 'jB2HCSSoph5AvSotat/roKYl+Xineb0MVCswtgtDyqo=',
        'User-Agent' : 'KakaoTalkAndroid/3.8.7 Android/4.1.2',
        'X-Requested-With' : 'XMLHttpRequest',
        'Referer': 'http://watcha.net/tutorial/how-to-eval',
        'Cookie' : 'watcha_fb_joined=true; __uvt=; fbm_126765124079533=base_domain=.watcha.net; autologin_auth_key=---+%0A%3Aid%3A+398608%0A%3Atoken%3A+%246%24MsNGylFY%24trORVbHvy8nr.okaQQk2S0A8DOqrMeUqo7nGN9jKow8U.eNYxZrg6gYgE05.o.l4h1AUxQXhGsFGw.HrzssWL%2F%0A; edu=%7B%7D; _guinness_session=BAh7CkkiD3Nlc3Npb25faWQGOgZFRkkiJWVmYThjYjYwYzM1MzhlMTRkMWJiYmY1NWE4MGQ2NGJiBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXFlOGxjOGI5R1BTNXBEbUhwekRVMGxuMjI3YWkwRHZTZUdnL3RZVERZRlk9BjsARkkiDHVzZXJfaWQGOwBGaQMQFQZJIhFhYl90ZXN0X2hhc2gGOwBGewBJIgtldmVudHMGOwBGewA%3D--e721b9b589414bb3034542aececf6aa7690e223b; request_method=GET; uvts=qE4EL6COSXWjBoE; __utma=59143211.741567025.1384285523.1384867187.1384878100.8; __utmb=59143211.104.3.1384881673653; __utmc=59143211; __utmz=59143211.1384285523.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=59143211.|1=Member%20Type=member=1^2=Join%20year%2Fmonth=2013%2F11=1^3=Join%20day=19=1^4=Member%20Id=igkP6JZ5QfyP=1^5=Ip=221.161.111.25=1',
        'Cache-Control' : 'no-cache',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Content-Length' : '0' }

    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request)
    r = response.read()
    print r

import json
j=json.loads(open('watcha_total.json','r').read())
j=j[40000:]
import thread
import time
for index,i in enumerate(j):
  print " ["+str(index)+"] id : " + i['id'] + " : " + i['title']
  #thread.start_new_thread(make_star,(i['id'],))
  make_star(i['id'])
