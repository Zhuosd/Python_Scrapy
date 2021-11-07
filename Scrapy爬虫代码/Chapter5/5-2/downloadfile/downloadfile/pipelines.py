# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request

class DownloadfilePipeline(FilesPipeline):
    # 修改file_path方法，使用提取的文件名保存文件
    def file_path(self, request, response=None, info=None):
        # 获取到Request中的item
        item = request.meta['item']
        # 文件URL路径的最后部分是文件格式
        file_type = request.url.split('.')[-1]
        # 修改使用item中保存的文件名作为下载文件的文件名，文件格式使用提取到的格式
        file_name = u'full/{0}.{1}'.format(item['file_name'],file_type)
        return file_name

    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            # 为request带上meta参数，把item传递过去
            yield Request(file_url,meta={'item':item})
