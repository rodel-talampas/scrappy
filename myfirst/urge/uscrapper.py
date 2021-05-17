import logging
import sys
import os

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import RetailItems

class QcrawlSpider(CrawlSpider):
    name = 'qCrawl'
    allowed_domains = ['theurge.com']
    start_urls = ['https://theurge.com/']
    deny_urls = ['https://theurge.com/page/faq']

    custom_settings = {
        'FEED_EXPORT_BATCH_ITEM_COUNT': 20,
        'FEEDS' : {
            'sale-%(batch_id)d.jl' : {
                'format' : 'jl',
                'store_empty' : True,
                'overwrite': True
            }
        }
    } 

    rules = (
        # Rule(LinkExtractor(allow=r'page/.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/*',deny=deny_urls), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = RetailItems()
        # item['title'] = response.xpath("//article[@class='_2Mqpk']").extract()
        item['salePrice'] = response.css('div.eP0wn._2xJnS::text').extract()
        # item['salePrice'] = response.xpath("//article/a/div[starts-with(@class,'eP0wn')]/text()").extract()
        item['price'] = response.xpath("//article/a/div[starts-with(@class,'eP0wn')]/span/text()").extract()
        item['brand'] = response.xpath("//article/a/p/span/text()").extract()
        item['description'] = response.xpath("//article/a/p/text()").extract()
        # item['salePrice'] = response.css('div.tags a.tag::text').getall()
        # item['description'] = response.xpath("//article/text()").extract()
        
        # item['category'] =response.css('span.text::text').extract()
        yield item

def scrap():
    logging.debug("This is a test scrap...")
    q = QcrawlSpider()

if __name__ == '__main__':
    # it is also possible to enable the API directly
    logging.basicConfig(filename='scrapper.log',level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    scrap()
