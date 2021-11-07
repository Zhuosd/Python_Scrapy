# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.exceptions import DropItem
import datetime

class IthomePipeline(object):
    # 定义集合ithome_news
    collection = 'ithome_news'

    def __init__(self,mongo_uri,mongo_db,stats):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.stats = stats

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            # 从settings.py中获取到MONGODB数据库连接信息，数据统计参数
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            stats=crawler.stats,
        )

    # 爬虫启动时打开数据库
    def open_spider(self,spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        # 开启爬虫时将结束时间写入数据集参数start中
        self.stats.set_value('start', datetime.datetime.now())

    # 爬虫关闭时关闭数据库连接
    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        # 如果抓取得item中含有title，则为有效数据，保存，否则丢弃
        if not item['title']:
            raise DropItem("数据不完整，丢弃：{}".format(item))
        else:
            self.db[self.collection].insert_one(dict(item))
        return item

