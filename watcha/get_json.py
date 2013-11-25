import urllib, urllib2


def make_json(page):
    print "[$] START GET"
    url = 'http://watcha.net/api/movies?type=eval&count=900&usercode=igkP6JZ5QfyP&page='+str(page)+'&more=true'

    headers = { 'POST' : '/api/movies/?type=eval&count=900&usercode=igkP6JZ5QfyP&page='+str(page)+'&more=true',
        'HOST' : 'watcha.net',
        'Connection' : 'Close',
        'Proxy-Connection': 'keep-alive',
        'Accept' : '*/*',
        'Origin' : 'http://watcha.net',
        'X-CSRF-Token' : 'jB2HCSSoph5AvSotat/roKYl+Xineb0MVCswtgtDyqo=',
        'User-Agent' : 'KakaoTalkAndroid/3.8.7 Android/4.1.2',
        'X-Requested-With' : 'XMLHttpRequest',
        'Referer': 'http://watcha.net/tutorial/how-to-eval',
        'Cookie' : 'watcha_fb_joined=true; __uvt=; fbm_126765124079533=base_domain=.watcha.net; autologin_auth_key=---+%0A%3Aid%3A+398608%0A%3Atoken%3A+%246%24MsNGylFY%24trORVbHvy8nr.okaQQk2S0A8DOqrMeUqo7nGN9jKow8U.eNYxZrg6gYgE05.o.l4h1AUxQXhGsFGw.HrzssWL%2F%0A; _guinness_session=BAh7DUkiD3Nlc3Npb25faWQGOgZFRkkiJTNkNzI5MTk4ODA0ZWJmMDc0YWQyNDJkMGQ4ZjhlMGJmBjsAVEkiEWFiX3Rlc3RfaGFzaAY7AEZ7AEkiEF9jc3JmX3Rva2VuBjsARkkiMWpCMkhDU1NvcGg1QXZTb3RhdC9yb0tZbCtYaW5lYjBNVkNzd3RndER5cW89BjsARkkiC2V2ZW50cwY7AEZ7AEkiCnNwbGl0BjsARnsASSIMdXNlcl9pZAY7AEZpAxAVBkkiE2hvd3RvZXZhbF9zdGVwBjsARmkGSSIZdHV0b3JpYWxfbGlzdF9yZXBlYXQGOwBGaQA%3D--00397447bb4d515bcebe9b2fb6457ddef5e6ef7d; uvts=qE4EL6COSXWjBoE; request_method=POST; __utma=59143211.741567025.1384285523.1384830632.1384830882.5; __utmb=59143211.77.3.1384845138743; __utmc=59143211; __utmz=59143211.1384285523.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=59143211.|1=Member%20Type=member=1^2=Join%20year%2Fmonth=2013%2F11=1^3=Join%20day=19=1^4=Member%20Id=igkP6JZ5QfyP=1^5=Ip=221.161.111.25=1',
        'Cache-Control' : 'no-cache',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Content-Length' : '0' }

    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request)
    r = response.read()
    return r

import json
#2902
import thread
import time
#for i in range(2,15):
#for i in range(15,60):
for i in range(60,70):
  print " [" + str(i) + "]"
  j=make_json(i)
  f=open('json'+str(i*900)+'.json','w')
  f.write(j)
  f.close()
