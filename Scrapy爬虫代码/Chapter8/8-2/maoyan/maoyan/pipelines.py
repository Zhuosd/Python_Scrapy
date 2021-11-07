# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MaoyanPipeline(object):
    # 爬虫启动时创建文件maoyan.json
    def open_spider(self,spider):
        self.file = open('maoyantop100.json', 'w')

    # 爬虫关闭时关闭文件
    def close_spider(self,spider):
        self.file.close()

    # 将抓取数据写入json文件
    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
