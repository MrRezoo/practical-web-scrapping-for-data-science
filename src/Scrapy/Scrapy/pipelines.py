# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import sqlite3


class ScrapyPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.cnt = sqlite3.connect('quote.db')
        self.cur = self.cnt.cursor()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS quote(
                    title MESSAGE_TEXT ,
                    author MESSAGE_TEXT,
                    tags TEXT 
                );
        """)

    def store_data(self, item):
        self.cur.execute(
            'INSERT INTO quote(title, author,tags) VALUES(?, ?, ?)',
            (item['title'], item['author'], item['tags'][1]))
        self.cnt.commit()

    """ if you want to disable or enable pipeline /settings.py line 65-68"""

    def process_item(self, item, spider):
        self.store_data(item)
        return item

    # ----------------------- to analyse and change data

    # if len(item.get('tags')) >= 2:
    #     item['tags'] = item['tags'][:2]
    #     self.store_data(item)
    #     return item
    # else:
    #     raise DropItem('Sorry, this quote has fewer tags...')
