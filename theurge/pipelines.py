# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter

class TheurgePipeline:
    def process_item(self, item, spider):
        return item


class EmptyItemPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if not adapter['salePrice'] and not adapter['price'] \
            and not adapter['brand'] and not adapter['description'] and not adapter['category']:
            raise DropItem(f"Empty Item: {item!r}")
        else:
            return item

class ItemCountPipeline:
    def process_item(self, item, spider):
        if spider.total_items >= spider.total_item_to_extract:
            raise DropItem(f"Empty Item: {item!r}")
        else:
            spider.total_items = spider.total_items + 1
            return item