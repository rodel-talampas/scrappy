# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    salePrice = scrapy.Field()
    description = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
    website = scrapy.Field()

    # Housekeeping fields
    url = scrapy.Field()
    category_param = scrapy.Field()
    brand_param = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()

    pass
