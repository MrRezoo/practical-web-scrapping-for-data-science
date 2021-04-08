# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ScrapyPipeline:
    """ if you want to disable or enable pipeline /settings.py line 65-68"""

    def process_item(self, item, spider):
        if len(item.get('tags')) >= 2:
            item['tags'] = item['tags'][:2]
            return item
        else:
            raise DropItem('Sorry, this quote has fewer tags...')
