from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.item import Item, Field

class ScrapyItem(Item):
    title = Field()
    url = Field()
    year = Field()
    country = Field()
    #director = Field()
    #company = Field()
    #actor = Field()
    genre= Field()

url = "http://movie.naver.com/movie/sdb/browsing/bmovie.nhn?year=2013&page=1"

index = 0
old_index = -1
loop = 0

class ScrapyOrgSpider(BaseSpider):
    name = "naver"
    allowed_domains = ["movie.naver.com"]
    start_urls = [url]

    def parse(self, response):
        global index, loop
        hxs = HtmlXPathSelector(response)
        items = []

        loop += 1

        next_page = ["http://movie.naver.com/movie/sdb/browsing/bmovie.nhn?year=2013&page="+str(loop)]

        if not not next_page:
            yield Request(next_page[0], self.parse)

        #posts = hxs.select("//tr")
        posts = hxs.select("//ul[@class='directory_list']/li")

        count = 0
        print "================= " + str(len(posts))
        print "[ " + str(loop) + " ] index : " + str(index)
        for post in posts:
            try:
              title = post.select("a/text()")[0].extract()
              url = post.select("a/@href")[0].extract()
              year = post.select("ul[@class='detail']/li/a/b/text()")[0].extract()
              country = post.select("ul[@class='detail']/li/a/text()")[0].extract()
              genre = post.select("ul[@class='detail']/li/a/text()")[1].extract()
              #director = 
              #company = post.select("td")[3].select("text()")[0].extract()
              #actor = post.select("td")[4].select("text()")[0].extract()
              #genre = post.select("td")[5].select("text()")[0].extract()
              count += 1
            except:
              continue

            item = ScrapyItem()
            item["title"] = title
            item["url"] = url
            item["year"] = year
            item["country"] = year
            #item["director"] = director
            #item["company"] = company
            #item["actor"] = actor
            item["genre"] = genre
            items.append(item)

        for item in items:
            yield item

        old_index = index
        index += count

        if count == 0:
            return
