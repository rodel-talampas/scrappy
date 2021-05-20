import datetime
import socket
from urllib import parse

# This is a super class that adds keeper information
class Keeper():

    def add_keeper_info(self, item, response):
        # Housekeeping fields
        item['url'] = response.url
        item['project'] = self.settings.get('BOT_NAME')
        item['spider'] = self.name
        item['server'] = socket.gethostname()
        item['date'] = datetime.datetime.now()

        params = dict(parse.parse_qsl(parse.urlsplit(response.url).query))
        item['category_param'] = params.get('cat', None)
        item['brand_param'] = params.get('brands', None)
        return item
