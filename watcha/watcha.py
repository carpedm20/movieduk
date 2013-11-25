import urllib

count = 0
max_count = 6#0000
base_url = "http://watcha.net/movies/detail/"
urls = [base_url + str(i) for i in range(max_count)]

for u in urls:
 r = urllib.urlopen(u)
  
 print r.geturl()
