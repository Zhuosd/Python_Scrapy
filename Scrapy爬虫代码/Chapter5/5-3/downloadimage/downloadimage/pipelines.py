# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DownloadimagePipeline(object):
    # 将小说信息保存为json文件
    def open_spider(self,spider):
        self.file = open('qidian.json','w')

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        # 写入文件
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item