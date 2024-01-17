import scrapy
from ..items import ScrapyworkItem

class UniSpider(scrapy.Spider): #Use "scrapy crawl uni" to run and create a txt file
    name = "uni"
    start_urls = ["https://www.shanghairanking.com/rankings/arwu/2023"]

    def parse(self, response):
        for row in response.css('tr[data-v-ae1ab4a8]'):
            item = ScrapyworkItem()
            #ALl the data we want : 
            item['univname'] = row.css('td.align-left div.global-univ span.univ-name::text').get()
            item['rank'] = row.css('td div.ranking::text').get()
            item['score'] = row.css('td:nth-child(5)::text').get()


            #self.log(f"university name: {item['univname']}")
            yield item
