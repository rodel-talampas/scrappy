import logging
import sys
import os

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import QuoteItems

class QcrawlSpider(CrawlSpider):
    name = 'qCrawl'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    custom_settings = {
        'FEED_EXPORT_BATCH_ITEM_COUNT': 20,
        'FEEDS' : {
            'quote-%(batch_id)d.jl' : {
                'format' : 'jl',
                'store_empty' : True,
                'overwrite': True
            }
        }
    } 

    rules = (
        Rule(LinkExtractor(allow=r'page/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = QuoteItems()
        item['quote'] =response.css('span.text::text').extract()
        item['author'] = response.css('small.author::text').extract()
        item['tags'] = response.css('div.tags a.tag::text').extract()
        yield item

def scrap():
    logging.debug("This is a test scrap...")
    q = QcrawlSpider()

if __name__ == '__main__':
    # it is also possible to enable the API directly
    logging.basicConfig(filename='scrapper.log',level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    scrap()
