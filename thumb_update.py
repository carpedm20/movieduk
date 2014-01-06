from core.models import *
import urllib2
from bs4 import BeautifulSoup

actors = Actor.objects.exclude(code=-1).filter(code__gte = 17404).order_by('code')

# 17405
count = 0
for a in actors:
  count += 1

  print "====================================="
  print a.code
  print a.thumb_url

  if a.thumb_url.find('77x96') != -1:
    a.thumb_url = a.thumb_url.replace('77x96','111x139')
    a.save()
    print "----------------------------------------"
    print a.thumb_url

  if a.thumb_url == '':
    r = urllib2.urlopen('http://movie.naver.com/movie/bi/pi/basic.nhn?code=' + str(a.code))
    try:
      soup = BeautifulSoup(r.read())

      img_url = soup.find('div','poster').img['src']
      if img_url.find('dft_img') != -1:
        continue
      else:
        a.thumb_url = img_url.replace('120x150','111x139').replace('77x96','111x139')
        a.save()
        print "******************************************"
        print a.thumb_url
    except:
      continue
