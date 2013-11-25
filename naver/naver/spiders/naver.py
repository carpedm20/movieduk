__author__ = 'carpedm20'
__date__ = '2013.11.14'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.item import Item, Field

import sys, os

class ScrapyItem(Item):
    title = Field()
    url = Field()
    year = Field()
    open1 = Field() # 2013
    open2 = Field() # 06.12
    country = Field()
    genre = Field()
    form = Field()
    grade = Field()

YEAR = "2015"
START_PAGE = 10 # 0
START_PAGE = 0 # 0
MAX_LOOP = 4 #-1
MAX_LOOP = -1 #-1
PMOD = True
PMOD = False

print "==================="
print YEAR
print "==================="

url = "http://movie.naver.com/movie/sdb/browsing/bmovie.nhn?year="+YEAR+"&page=" + str(START_PAGE)

index = start_page = START_PAGE
old_index = -1
old_title = ""
loop = 0
pmod = PMOD
max_loop = MAX_LOOP

class ScrapyOrgSpider(BaseSpider):
    name = "naver"
    allowed_domains = ["movie.naver.com"]
    start_urls = [url]

    def parse(self, response):
        global start_page, index, loop, old_title, pmod, max_loop

        hxs = HtmlXPathSelector(response)
        items = []

        loop += 1

        next_page = ["http://movie.naver.com/movie/sdb/browsing/bmovie.nhn?year="+YEAR+"&page="+str(loop + start_page)]

        if max_loop != -1:
          if loop >= max_loop:
              next_page = []

        posts = hxs.select("//ul[@class='directory_list']/li")
        title = posts[0].select("a/text()")[0].extract()

        if old_title == title and loop > 2:
          next_page = []
        else:
          old_title = title

        if not not next_page:
            yield Request(next_page[0], self.parse)

        #posts = hxs.select("//tr")

        count = 0
        print "[ " + str(loop) + " ] index : " + str(index) + ", len(posts) : " + str(len(posts))

        for post in posts:
            try:
              title = post.select("a/text()")[0].extract()
              if pmod: print " [ " + str(count) + " ] TITLE : " + title
              url = post.select("a/@href")[0].extract()
              if pmod: print " [ " + str(count) + " ] URL : " + url 
              year = post.select("ul[@class='detail']/li/a")[0].select("b/text()")[0].extract()
              if pmod: print " [ " + str(count) + " ] YEAR : " + year

              open1 = ""
              open2 = ""
              country = ""
              genre = ""
              form = ""
              grade = ""

              open_count = 0
              lis = post.select("ul[@class='detail']/li/a")

              for li in lis:
                h = li.select('@href')[0].extract()
                href = h[h.find('&')+1:h.rfind('=')]
                if pmod: print " [*] HREF : " + href

                if href == '?year':
                  if pmod: print "  [-] HREF SKIP : " + h
                  continue

                if href == 'open' and open_count == 0:
                  open1 = li.select('text()')[0].extract()
                  open_count += 1
                  if pmod: print " [*] open1 : " + open1
                elif  href == 'open' and open_count == 1:
                  try:
                    open2 = li.select('text()')[0].extract()
                    if pmod: print " [*] open2 : " + open2
                  except:
                    z = 123
                elif href == 'nation':
                  country = li.select('text()')[0].extract()
                  if pmod: print " [*] country : " + country
                elif href == 'genre':
                  genre = li.select('text()')[0].extract()
                  if pmod: print " [*] genre : " + genre
                elif href == 'form':
                  form = li.select('text()')[0].extract()
                  if pmod: print " [*] form : " + form
                elif href == 'grade':
                  grade = li.select('text()')[0].extract()
                  if pmod: print " [*] grade : " + grade 
                else:
                  print " [^] Found NEW href : " + h
                  return

              count += 1
            except Exception as e:
              #for frame in traceback.extract_tb(sys.exc_info()[2]):
              #  fname,lineno,fn,text = frame
              #  print "Error in %s on line %d" % (fname, lineno)
              exc_type, exc_obj, exc_tb = sys.exc_info()
              fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
              print(exc_type, fname, exc_tb.tb_lineno)
              #for e in sys.exc_info():
              #  print e
              continue

            item = ScrapyItem()
            item["title"] = title
            item["url"] = url
            item["year"] = year
            item["open1"] = open1
            item["open2"] = open2
            item["country"] = country
            item["genre"] = genre
            item["form"] = form
            item["grade"] = grade
            items.append(item)

        for item in items:
            yield item

        old_index = index
        index += count
