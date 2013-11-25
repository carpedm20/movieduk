__author__ = 'carpedm20'
__date__ = '2013.11.14'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.item import Item, Field

import json
import sys, os

#http://watcha.net/api/movies?type=eval&count=24&usercode=igkP6JZ5QfyP
#http://watcha.net/api/movies?type=eval&count=1000&usercode=igkP6JZ5QfyP&page=2&more=true

########## FAIL #############
#base = "http://watcha.net/api/movies?type=eval&count=900&usercode=igkP6JZ5QfyP&more=true&page="
#base = "http://watcha.net/api/movies?type=eval&count=100&usercode=igkP6JZ5QfyP&more=true&page="

######### SUCCESS #############
#base = "http://watcha.net/api/movies?type=eval&count=24&usercode=igkP6JZ5QfyP&more=true&page="
base = "http://watcha.net/api/movies?type=eval&count=24&more=true&page="


count = 0

class ScrapyOrgSpider(BaseSpider):
    name = "watcha3"
    allowed_domains = ["watcha.net"]

    def start_requests(self):
      global base, count
      try:
        #for url in self.start_urls:
        for i in range(2,9):
          url = base +str(i)
          print "========================>>>>>>> " + url
          yield Request(url,cookies={ "_guinness_session":"BAh7CUkiD3Nlc3Npb25faWQGOgZFRkkiJWVmYThjYjYwYzM1MzhlMTRkMWJiYmY1NWE4MGQ2NGJiBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXFlOGxjOGI5R1BTNXBEbUhwekRVMGxuMjI3YWkwRHZTZUdnL3RZVERZRlk9BjsARkkiDHVzZXJfaWQGOwBGaQMQFQZJIhFhYl90ZXN0X2hhc2gGOwBGewA%3D--088a53f2b1c91815bbb914b36f03740f35a51d2f;"})
      except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    def parse(self, response):
      global count
      try:
         count += 1
         f=open('watcha_json'+str(count)+'.json','w')
         f.write(response.body)
         f.close()
         print "========>>>>>>> " + response.url
      except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
