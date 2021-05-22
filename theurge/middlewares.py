# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from datetime import datetime
from scrapy.exceptions import IgnoreRequest

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class TheurgeSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('mid -> Spider opened: %s' % spider.name)

    def spider_closed(self, spider):
        spider.logger.info('mid -> Spider closed: %s' % spider.name)


class TheurgeDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    request_time = None
    response_time = None

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        self.request_time = datetime.now()

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        self.response_time = datetime.now()
        difference = self.response_time - self.request_time
        spider.logger.info('Download (minutes, seconds): %s' % (divmod(difference.total_seconds(), 60),) )

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain

        pass

    def spider_opened(self, spider):
        spider.logger.info('mid download -> Spider opened: %s' % spider.name)

    def spider_closed(self, spider):
        spider.logger.info('mid download -> Spider closed: %s' % spider.name)

class TheurgeItemCountMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self, total_item_to_extract):
        self.total_items = 0
        self.total_item_to_extract = total_item_to_extract

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.

        # get the interval of items from settings
        total_item_to_extract = crawler.settings.getint('TOTAL_ITEMCOUNT', 300)

        s = cls(total_item_to_extract)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        if self.total_items > self.total_item_to_extract:
            spider.logger.info('Spider has hit the maximum number of items processed')
            raise IgnoreRequest('Spider has hit the maximum number of items processed')

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        self.total_items = self.total_items + 1
        spider.logger.info('Count %s ' % self.total_items)

        # if self.total_items > self.total_item_to_extract:
        #     spider.logger.info('Spider has hit the maximum number of items processed')
        #     raise IgnoreRequest('Spider has hit the maximum number of items processed')

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain

        pass

    def spider_opened(self, spider):
        spider.logger.info('mid download -> Spider opened: %s' % spider.name)
        self.total_items = 0

    def spider_closed(self, spider):
        spider.logger.info('mid download -> Spider closed: %s' % spider.name)        
