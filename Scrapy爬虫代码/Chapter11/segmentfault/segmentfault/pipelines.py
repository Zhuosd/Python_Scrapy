# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class SegmentfaultPipeline(object):
    # 设定MongoDB集合名称
    collection_name = 'userinfo'

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    # 通过crawler获取settings.py中设定的MongoDB连接信息
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB','segmentfault')
        )

    # 当爬虫启动时连接MongoDB
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    # 当爬虫关闭时断开MongoDB连接
    def close_spider(self,spider):
        self.client.close()

    # 将Item插入数据库保存
    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


