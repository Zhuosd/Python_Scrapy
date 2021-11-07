# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class LianjiahousePipeline(object):
    # 设置存储文档名称
    collection_name = 'lianjiahouse'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            # 通过crawler获取settings文件，获取其中的MongoDB配置信息
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'lianjia')
        )

    def open_spider(self, spider):
        # 当爬虫打开时连接MongoDB数据库
        # 先连接server，在连接指定数据库
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        # 爬虫结束时关闭数据库连接
        self.client.close()

    def process_item(self, item, spider):
        # 将item插入数据库
        self.db[self.collection_name].insert(dict(item))
        return item


class LianjiaImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['images_urls']:
            # 将图片地址传入Request，进行下载，同时将item做参数添加到Request中
            yield Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        # 从Request中获取item，以房屋标题做文件夹名称
        item = request.meta['item']
        image_folder = item['house_name']
        # 使用图片url做图片存储名称
        image_guild = request.url.split('/')[-1]
        # 图片保存，文件夹/图片
        image_save = u'{0}/{1}'.format(image_folder, image_guild)
        return image_save