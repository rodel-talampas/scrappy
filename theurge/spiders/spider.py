import datetime
import socket
import yaml
import os

# This is a super class that adds keeper information
class Keeper():

    def add_keeper_info(self, item, response):
        # Housekeeping fields
        item['url'] = response.url
        item['project'] = self.settings.get('BOT_NAME')
        item['spider'] = self.name
        item['server'] = socket.gethostname()
        item['date'] = datetime.datetime.now()
        return item
