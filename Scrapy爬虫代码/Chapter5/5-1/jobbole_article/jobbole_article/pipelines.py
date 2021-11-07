# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class JobboleArticlePipeline(object):
    # 当启动爬虫时，打开items.json文件，准备写入数据
    def open_spider(self, spider):
        self.file = open('items.json','w')

    # 当爬虫执行结束时，关闭打开的文件
    def close_spider(self, spider):
        self.file.close()

    # 将抓取到的数据做json序列化存储
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

