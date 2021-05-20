from scrapy import signals
from scrapy.exceptions import NotConfigured

import logging
import json
from datetime import datetime

seconds_in_day = 24 * 60 * 60

class TheurgeStatsLogging:

    def __init__(self, interval):
        self.interval = interval
        self.start_time = datetime.now()
        self.stats = {}
        self.logger = None

    @classmethod
    def from_crawler(cls, crawler):
        # first check if the extension should be enabled and raise
        # NotConfigured otherwise
        if not crawler.settings.getbool('STATS_LOGGING_EXTENSION_ENABLED'):
            raise NotConfigured

        # get the interval of items from settings
        stats_interval = crawler.settings.getfloat('LOGSTATS_INTERVAL', 60.0)

        # instantiate the extension object
        ext = cls(stats_interval)

        # connect the extension object to signals
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)

        # return the extension object
        return ext

    def spider_opened(self, spider):
        self.logger = logging.getLogger(spider.name)
        self.logger.info("ext -> Spider opened: %s", spider.name)

    def spider_closed(self, spider):
        self.logger.info("ext -> Spider closed: %s", spider.name)
        self.logger.debug("Displaying final Stats after Process ....")
        self.logger.info("scraped items test")

    def display_stats(self):
        self.logger.info("===============================================")
        self.logger.info(json.dumps(self.stats, indent = 3))
        self.logger.info("===============================================")

    def item_scraped(self, item, spider):
        this_time = datetime.now()
        difference = this_time - self.start_time
        category = ''
        if item['category_param']:
            category = item['category_param']
        elif item['category']:
            category = item['category']
        elif item['brand_param']:
            category = item['brand_param']
        elif item['brand']:
            category = item['brand']
        
        if category in self.stats:
            self.logger.info('%s exists' % category)
            self.stats[category] = int (self.stats[category]) + 1
        else:
            self.stats[category] = 1

        if int(divmod(difference.total_seconds(), self.interval)[1]) == 0:
            self.display_stats()