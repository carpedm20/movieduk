__author__ = 'carpedm20'
__date__ = '2013.11.14'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.item import Item, Field

import sys, os

class ScrapyItem(Item):
  id = Field()
  title = Field()
  year = Field()

count = 80000
max_count = 100000
base_url = "http://watcha.net/movies/detail/"
urls = [base_url + str(i) for i in range(count, max_count)]

class ScrapyOrgSpider(BaseSpider):
    global urls
    name = "watcha"
    allowed_domains = ["watcha.net"]
    start_urls = urls

    def parse(self, response):
      global count

      items=[]

      url = response.url
      id = url[url.rfind('/')+1:]
      title = url[url.find('mv/')+3:url.rfind('/')]
      year = title[title.rfind('-')+1:]
      
      if year.isdigit():
        print " - " + str(count) + "  > " + title[:title.rfind('-')] + " : " + year
        item = ScrapyItem()
        item["title"] = title
        item["id"] = id
        item["year"] = year
        count += 1

        items.append(item)

        if url.find('basic') != -1:
          return
        else:
          for item in items:
            yield item
