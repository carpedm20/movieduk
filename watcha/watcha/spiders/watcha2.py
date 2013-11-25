__author__ = 'carpedm20'
__date__ = '2013.11.14'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.item import Item, Field

import json
import sys, os

base_url = "http://watcha.net/movies/detail/"
j=json.loads(open('watcha_total.json','r').read())
j=j[1870:]

urls = ["http://watcha.net/eval/movie/"+i['id']+"/5" for i in j]

cookies = "watcha_fb_joined=true; __uvt=; fbm_126765124079533=base_domain=.watcha.net; autologin_auth_key=---+%0A%3Aid%3A+398608%0A%3Atoken%3A+%246%24MsNGylFY%24trORVbHvy8nr.okaQQk2S0A8DOqrMeUqo7nGN9jKow8U.eNYxZrg6gYgE05.o.l4h1AUxQXhGsFGw.HrzssWL%2F%0A; _guinness_session=BAh7DUkiD3Nlc3Npb25faWQGOgZFRkkiJTNkNzI5MTk4ODA0ZWJmMDc0YWQyNDJkMGQ4ZjhlMGJmBjsAVEkiEWFiX3Rlc3RfaGFzaAY7AEZ7AEkiEF9jc3JmX3Rva2VuBjsARkkiMWpCMkhDU1NvcGg1QXZTb3RhdC9yb0tZbCtYaW5lYjBNVkNzd3RndER5cW89BjsARkkiC2V2ZW50cwY7AEZ7AEkiCnNwbGl0BjsARnsASSIMdXNlcl9pZAY7AEZpAxAVBkkiE2hvd3RvZXZhbF9zdGVwBjsARmkGSSIZdHV0b3JpYWxfbGlzdF9yZXBlYXQGOwBGaQA%3D--00397447bb4d515bcebe9b2fb6457ddef5e6ef7d; uvts=qE4EL6COSXWjBoE; request_method=POST; __utma=59143211.741567025.1384285523.1384830632.1384830882.5; __utmb=59143211.77.3.1384845138743; __utmc=59143211; __utmz=59143211.1384285523.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=59143211.|1=Member%20Type=member=1^2=Join%20year%2Fmonth=2013%2F11=1^3=Join%20day=19=1^4=Member%20Id=igkP6JZ5QfyP=1^5=Ip=221.161.111.25=1"

class ScrapyOrgSpider(BaseSpider):
    global urls
    name = "watcha2"
    allowed_domains = ["watcha.net"]
    start_urls = urls

    def start_requests(self):
      try:
        for url in self.start_urls:
          yield Request(url, cookies={'_guinness_session':'BAh7DUkiD3Nlc3Npb25faWQGOgZFRkkiJTNkNzI5MTk4ODA0ZWJmMDc0YWQyNDJkMGQ4ZjhlMGJmBjsAVEkiEWFiX3Rlc3RfaGFzaAY7AEZ7AEkiEF9jc3JmX3Rva2VuBjsARkkiMWpCMkhDU1NvcGg1QXZTb3RhdC9yb0tZbCtYaW5lYjBNVkNzd3RndER5cW89BjsARkkiC2V2ZW50cwY7AEZ7AEkiCnNwbGl0BjsARnsASSIMdXNlcl9pZAY7AEZpAxAVBkkiE2hvd3RvZXZhbF9zdGVwBjsARmkGSSIZdHV0b3JpYWxfbGlzdF9yZXBlYXQGOwBGaQA%3D--00397447bb4d515bcebe9b2fb6457ddef5e6ef7d'})
      except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    def parse(self, response):
      try:
         print "========>>>>>>> " + response.url
      except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
