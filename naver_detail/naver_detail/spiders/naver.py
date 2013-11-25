__author__ = 'carpedm20'
__date__ = '2013.11.14'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.item import Item, Field

import sys, os
import json
import urllib
from ast import literal_eval
from md5 import md5

from config import cookies

f = open('movie_simple_for_django.json', 'r')
r = f.read()
j = json.loads(r)

#j=j[90000:90090]
#j=j[0:20000]
#j=j[20000:40000]
#j=j[40000:80000]
j=j[0:96790]

def download_pic(url,year,country_code):
 try:
  year = year.strip()

  if url.find('dft_img') != -1:
    return False

  if url.rfind('naver.net') != -1:
    new_url = url[url.rfind('naver.net') + 9:]
    #print " [$] url : " + new_url
  else:
    new_url = url
    print " ===========> [$] url : " + url

  ex = url[url.rfind('.'):]
  if ex.find('?') != -1:
    url = url[:url.rfind('?')]
    ex = ex[:ex.find('?')]

  directory = './tmp/'+year+'/'+country_code
  #print "directory : " + directory

  try:
    #urllib.urlretrieve(url, directory+'/pic_'+md5(new_url).hexdigest()+ex)
    z=123
  except:
    os.makedirs(directory)
    #urllib.urlretrieve(url, directory+'/pic_'+md5(new_url).hexdigest()+ex)

  return url
 except Exception as e:
  #for frame in traceback.extract_tb(sys.exc_info()[2]):
  #  fname,lineno,fn,text = frame
  #  print "Error in %s on line %d" % (fname, lineno)
  exc_type, exc_obj, exc_tb = sys.exc_info()
  fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
  print(exc_type, fname, exc_tb.tb_lineno)

class Movie(Item):
  actors = Field() # list string -> import ast; ast.literal_eval(actors)
  subActors = Field() # list string
  director = Field() # list string

  detail_url = Field()
  poster_url = Field()
  story1 = Field()
  story2 = Field()
  title1 = Field()
  title2 = Field()
  genre = Field()
  country = Field()
  country_code = Field()
  time = Field()
  year = Field()
  open = Field()

  grade = Field()

class Actor(Item):
  profile_url = Field()
  thumb_url = Field()
  name = Field()
  en_name = Field()
  part = Field()
  character = Field()

  career1_title = Field()
  career1_year= Field()
  career2_title = Field()
  career2_year= Field()

class SubActor(Item):
  profile_url = Field()
  name = Field()
  character = Field()

class Director(Item):
  profile_url = Field()
  thumb_url = Field()
  name = Field()
  en_name = Field()

PMOD = True
PMOD = False

#url = "http://movie.naver.com/movie/bi/mi/basic.nhn?code=10048"
base_url = "http://movie.naver.com"
index = 0

story1 = {} 
story2 = {}
poster_url = ''

class ScrapyOrgSpider(BaseSpider):
    name = "naver"
    allowed_domains = ["movie.naver.com"]

    basic_urls = ["http://movie.naver.com" + i['url'].encode('utf-8') for i in j]
    detail_urls = ["http://movie.naver.com" + i['url'].replace('basic','detail').encode('utf-8') for i in j]
    #start_urls = [url]
    start_urls = basic_urls + detail_urls

    print " ************************"
    print " *  NAVER MOVIE PARSER  *"
    print " *                      *"
    print " *      carpedm20       *"
    print " *                      *"
    print " ************************"
    print " [*] Length of urls : " + str(len(start_urls))
    print " ************************"
    print

    """
    def start_requests(self):
      #yield Request(urls[0], cookies={'store_language':'en'})

        #yield Request(url, callback=self.parse_category)
      for url in self.basic_urls:
        yield Request(url, cookies=cookies)

      for url in self.detail_urls:
        yield Request(url, cookies=cookies)
    """
    def parse(self, response):
     try:
        global index, story1, story2, url, poster_url

        hxs = HtmlXPathSelector(response)
        items = []

        url = response.url

        """
        if url.find('basic') != -1:
          next_url = url.replace('basic','detail')
        else:
          index += 1
          next_url = base_url + j[index]['url'].encode('utf-8')

        next_page = [next_url]

        if not not next_page:
          yield Request(next_page[0], self.parse)
        """
        index += 1

        if url.find('basic') != -1:
          print " BASIC : " + str(index) + " > " + response.url
          print " -----------------------------------------------------------"

          cur_url = response.url
          code = cur_url[cur_url.rfind('code=')+5:]
          try:
            story1[code] = hxs.select("//h5[@class='h_tx_story']/text()")[0].extract()
          except: 
            story1[code] = ""

          ps = hxs.select("//p[@class='con_tx']/text()").extract()

          try:
            story2[code] = ps[0]
            if len(ps) > 1:
              for p in ps[1:]:
                story2[code] += '<br>' + p
          except:
            story2[code] = ""

        else:
          print " DETAIL : " + str(index) + " > " + response.url
          print " ==========================================================="

          movie = Movie()

          cur_url = response.url
          code = cur_url[cur_url.rfind('code=')+5:]

          movie['detail_url'] = response.url

          try:
            movie['story1'] = story1[code]
          except:
            movie['story1'] = ''
          try:
            movie['story2'] = story2[code]
          except:
            movie['story1'] = ''

          try:
            poster_url = hxs.select("//div[@class='poster']/a/img/@src")[0].extract()
          except:
            poster_url = ""

          try:
            title = hxs.select("//h3[@class='h_movie']/a/text()")
            movie['title1'] = title[1].extract()
          except:
            print " ************* EXCEPTION *************"
            print response.url
            print " *************************************"

            f=open('error.txt','a')
            f.write(response.url+'\n')
            f.close()

          title2 = hxs.select("//strong[@class='h_movie2']/text()")
          movie['title2'] = title2 = title2[1].extract()
          year = title2[title2.rfind(',')+1:].strip()
          if year.isdigit() == False:
              year = "xxxx"
          movie['year'] = year

          infos = hxs.select("//dl[@class='info_spec']/dd")
          basics = infos[0].select('p/span')

          movie['genre'] = ''
          movie['open'] = ''
          movie['country'] = ''
          movie['country_code'] = country_code = 'XX'
          movie['time'] = ''
          movie['grade'] = ''

          for i in infos:
            try:
              href = i.select('p/a/@href')[0].extract()
              if href.find('?grade=') != -1:
                movie['grade'] = i.select('p/a/text()')[0].extract()
              else:
                z=123
            except:
              continue

          for b in basics:
            try:
              href = b.select('a/@href')[0].extract()
              if href.find('?genre=') != -1:
                genre = ''
                for g in b.select('a/text()'):
                  genre += g.extract() + ', '
                movie['genre'] = genre[:genre.rfind(',')]
              elif href.find('?open=') != -1:
                o = ''
                for g in b.select('a/text()'):
                  o += g.extract() + ', '
                try:
                  movie['open'] = o[:o.rfind(',')]
                except:
                  movie['open'] = ''
              elif href.find('?nation=') != -1:
                try:
                  movie['country'] = b.select('a/text()')[0].extract()
                except:
                  movie['country'] = ""
                try:
                  movie['country_code'] = country_code = href[href.find('?nation=') + 8:]
                except:
                  movie['country_code'] = "XX"
            except:
              try:
                movie['time'] = b.select('text()')[0].extract()
              except:
                z=123

          if poster_url != '':
            suc = download_pic(poster_url,year,country_code)

            if suc == False: poster_url = ""
            else: poster_url = suc

          movie['poster_url'] = poster_url

          result = list()

          actors = hxs.select("//ul[@class='lst_people']/li")

          for a in actors:
            actor = Actor()
            try:
              actor['profile_url'] = a.select('div/a/@href')[0].extract()
            except:
              actor['profile_url'] = ""

            try:
              actor['thumb_url'] = a.select('p/a/img/@src')[0].extract()
              suc = download_pic(actor['thumb_url'],year,country_code)
              if suc == False: actor['thumb_url'] = ""
              else: actor['thumb_url'] = suc
            except:
              actor['thumb_url'] = ""

            try:
              actor['name'] = a.select('div/span/text()')[0].extract()
            except:
              try:
                actor['name'] = a.select("div[@class='p_info']/a/text()")[0].extract()
              except:
                #print "==================>>>>>>>>>>>>>>>>>>"
                actor['name'] = ""

            try:
              actor['en_name'] = a.select("div[@class='p_info']/em/text()")[0].extract()
            except:
              actor['en_name'] = ""

            try:
              actor['part'] = a.select("div[@class='p_info']/div/p/em/text()")[0].extract()
            except:
              actor['part'] = ""

            try:
              actor['character'] = a.select("div[@class='p_info']/div/p/span/text()")[0].extract()
            except:
              actor['character'] = ""

            actor['career1_title'] = ""
            actor['career1_year'] = ""
            actor['career2_title'] = ""
            actor['career2_year'] = ""

            careers = a.select("div[@class='p_info']/ul/li")
            for i, c in enumerate(careers):
              if i == 0:
                actor['career1_title'] = a.select("div[@class='p_info']/ul/li")[0].select('a/text()')[0].extract()
                actor['career1_year'] = a.select("div[@class='p_info']/ul/li")[0].select('span/text()')[0].extract()
              elif i == 1:
                actor['career2_title'] = a.select("div[@class='p_info']/ul/li")[0].select('a/text()')[0].extract()
                actor['career2_year'] = a.select("div[@class='p_info']/ul/li")[0].select('span/text()')[0].extract()
            result.append(dict(actor))

          movie['actors'] = result
          result = list()

          sub_actors = hxs.select("//table[@id='subActorList']/tbody/tr/td/span")
          for s in sub_actors:
            sub = SubActor()
            try:
              sub['profile_url'] = s.select('a/@href')[0].extract()
            except:
              sub['profile_url'] = ""

            try:
              sub['name'] = s.select('a/text()')[0].extract()
            except: 
              sub['name'] = ""

            try:
              sub['character'] = s.select('em/text()')[0].extract()
            except:
              sub['character'] = ""
            result.append(dict(sub))

          movie['subActors'] = result
          result = list()

          directors = hxs.select("//div[@class='dir_obj']")
          for director in directors:
            d = Director()
            #profile_url = director.select("//p[@class='thumb_dir']/a/@href")[0].extract()
            try:
              d['thumb_url'] = director.select("p[@class='thumb_dir']/a/img/@src")[0].extract()
              suc = download_pic(d['thumb_url'],year,country_code)
              if suc == False: d['thumb_url'] = ""
              else: d['thumb_url'] = suc
            except:
              d['thumb_url'] = ""

            try:
              d['profile_url'] = director.select("div[@class='dir_product']/a/@href")[0].extract()
            except:
              d['profile_url'] = ""

            try:
              d['name'] = director.select("div[@class='dir_product']/a/text()")[0].extract()
            except:
              d['name'] = ""

            try:
              d['en_name'] = director.select("div[@class='dir_product']/em/text()")[0].extract()
            except:
              d['en_name'] = ""

            result.append(dict(d))

          movie['director'] = result

          #other_movies = director.select("//ul[@class='other_list']/li")
          #for m in other_movies:
          #  poster_url = m.select('p/a/img/@src')[0].extract()

          items.append(movie)

        if url.find('basic') != -1:
          return
        else:
          for item in items:
            yield item

     except Exception as e:
       #for frame in traceback.extract_tb(sys.exc_info()[2]):
       #  fname,lineno,fn,text = frame
       #  print "Error in %s on line %d" % (fname, lineno)
       exc_type, exc_obj, exc_tb = sys.exc_info()
       fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
       print(exc_type, fname, exc_tb.tb_lineno)
