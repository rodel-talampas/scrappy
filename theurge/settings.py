# Scrapy settings for theurge project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'theurge'

SPIDER_MODULES = ['theurge.spiders']
NEWSPIDER_MODULE = 'theurge.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'theurge (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'theurge.middlewares.TheurgeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'theurge.middlewares.TheurgeDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   'theurge.extensions.TheurgeStatsLogging': 500,
}

STATS_LOGGING_EXTENSION_ENABLED = True
LOGSTATS_INTERVAL = 5

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'theurge.pipelines.EmptyItemPipeline': 300,
   'theurge.pipelines.TheurgePipeline': 400,
}

FEED_EXPORT_BATCH_ITEM_COUNT = 20
FEEDS = {
    'sale-%(batch_id)d.jl' : {
                'format' : 'jl',
                'store_empty' : False,
                # These are the fields that will be included in the JL file/s. 
                # These fields needs to be defined in the items.py
                'fields': ['title','brand','description','price','salePrice','website'],
                'overwrite': True
            }
}
CLOSESPIDER_ITEMCOUNT=50
