import scrapy

class RetailItems(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    salePrice = scrapy.Field()
    description = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()