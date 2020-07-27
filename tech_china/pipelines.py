# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class MongoPipeline:
    """MongoDB存储"""
    def __init__(self, mongouri, mongodb, collection):
        self.mongo_uri = mongouri
        self.mongo_db = mongodb
        self.collection = collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongouri=crawler.settings.get('MONGO_URI'),
            # mongodb=crawler.settings.get('MONGO_DB'),
            # collection=crawler.settings.get('COLLECTION'),
            mongodb=crawler.settings.get('DIGI_MONGO_DB'),
            collection=crawler.settings.get('DIGI_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[self.collection].insert(dict(item))
        # self.db[self.collection].update_one({'title': item['title']}, {'$set': dict(item)}, upsert=True)
        return item

    def close_spider(self, spider):
        self.client.close()
