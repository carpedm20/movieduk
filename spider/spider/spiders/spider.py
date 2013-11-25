from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.item import Item, Field

class ScrapyItem(Item):
    title = Field()
    url = Field()
    year = Field()
    director = Field()
    company = Field()
    actor = Field()
    genre= Field()

url = "http://www.kmdb.or.kr/SearchSF1/totalsearch.asp?tabState=tabcolKOR&collection=colKOR&searchMode=3&searchDivision=all&befQuery=&reSearch=&detailsearch=no&exQuery=&filterOperation=%28PROD_YEAR%3Cgte%3E1900+PROD_YEAR%3Clte%3E2014%29+&collectionQuery=&v_field=ALL&openflag=N&selectmode=total&nil_Search=btn&searchText=&sortTarget=RANK&iSortOrder=1&startCnt=0&viewCntV=1000"

url = "http://www.kmdb.or.kr/SearchSF1/totalsearch.asp?tabState=tabcolFOR&collection=colFOR&searchMode=3&searchDivision=all&befQuery=&reSearch=&startCnt=0&detailsearch=no&exQuery=&filterOperation=%28PROD_YEAR%3Cgte%3E1900+PROD_YEAR%3Clte%3E2014%29+&collectionQuery=&v_field=ALL&openflag=N&selectmode=total&nil_Search=btn&searchText=&viewCntV=10"

url = "http://movie.naver.com/movie/sdb/browsing/bmovie.nhn?year=2013"

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

        #next_page = ["http://www.kmdb.or.kr/SearchSF1/totalsearch.asp?tabState=tabcolKOR&collection=colKOR&searchMode=3&searchDivision=all&befQuery=&reSearch=&detailsearch=no&exQuery=&filterOperation=%28PROD_YEAR%3Cgte%3E1900+PROD_YEAR%3Clte%3E2014%29+&collectionQuery=&v_field=ALL&openflag=N&selectmode=total&nil_Search=btn&searchText=&sortTarget=RANK&iSortOrder=1&viewCntV=1000&startCnt=" +str(index)]
        #next_page = ["http://www.kmdb.or.kr/SearchSF1/totalsearch.asp?tabState=tabcolFOR&collection=colFOR&searchMode=3&searchDivision=all&befQuery=&reSearch=&detailsearch=no&exQuery=&filterOperation=%28PROD_YEAR%3Cgte%3E1900+PROD_YEAR%3Clte%3E2014%29+&collectionQuery=&v_field=ALL&openflag=N&selectmode=total&nil_Search=btn&searchText=&sortTarget=RANK&iSortOrder=1&viewCntV=1000&startCnt=" +str(index)]
        next_page = ["http://movie.naver.com/movie/sdb/browsing/bmovie.nhn?year=2013&page="+str(loop)]

        if not not next_page:
            yield Request(next_page[0], self.parse)

        posts = hxs.select("//tr")

        count = 0
        print "[ " + str(loop) + " ] index : " + str(index)
        for post in posts:
            try:
              title = post.select("td[@class='ali_l']/a/text()")[0].extract()
              url = post.select("td[@class='ali_l']/a/@href")[0].extract()
              year = post.select("td")[1].select("text()")[0].extract()
              director = post.select("td")[2].select("text()")[0].extract()
              company = post.select("td")[3].select("text()")[0].extract()
              actor = post.select("td")[4].select("text()")[0].extract()
              genre = post.select("td")[5].select("text()")[0].extract()
              count += 1
            except:
              continue

            item = ScrapyItem()
            item["title"] = title
            item["url"] = url
            item["year"] = year
            item["director"] = director
            item["company"] = company
            item["actor"] = actor
            item["genre"] = genre
            items.append(item)

        for item in items:
            yield item

        old_index = index
        index += count

        if count == 0:
            return
