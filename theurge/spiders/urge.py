import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from theurge.items import RetailItem


class UrgeSpider(CrawlSpider):
    name = 'urge'
    allowed_domains = ['theurge.com']
    start_urls = ['https://theurge.com/women/search/?cat=accessories&brands=Emilio+Pucci']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = RetailItem()
        # item['title'] = response.xpath("//article[@class='_2Mqpk']").extract()
        item['salePrice'] = response.xpath("//*[@class='_2Mqpk']/a[1]/div[2]/text()[2]").get()
        # item['salePrice'] = response.xpath("//article/a/div[starts-with(@class,'eP0wn')]/text()").extract()
        item['price'] = response.css('div.eP0wn._2xJnS span._2plVT::text').get()
        item['brand'] = response.css("span.URfXD::text").get()
        item['description'] = response.xpath("//article/a/p/text()").get()       
        # item['category'] =response.css('span.text::text').extract()
        return item
