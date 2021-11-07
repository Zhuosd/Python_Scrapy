# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DownloadfileItem(scrapy.Item):
    # define the fields for your item here like:
    # 文件名
    file_name = scrapy.Field()
    # 发布时间
    release_date = scrapy.Field()
    # 文件url
    file_urls = scrapy.Field()
    # 文件结果信息
    files = scrapy.Field()
