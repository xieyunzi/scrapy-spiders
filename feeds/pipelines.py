# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class FeedsPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    def __init__(self, mongo_server, mongo_port, mongo_db):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db

        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGODB_SERVER'),
            mongo_port=crawler.settings.get('MONGODB_PORT'),
            mongo_db=crawler.settings.get('MONGODB_DB', 'scrapy'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mongo_server, port=self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        d_item = dict(item)
        if bool(d_item) and d_item.get('_collection'):
            collection = d_item.pop('_collection')
            self.db[collection].insert_one(d_item)
        return item
