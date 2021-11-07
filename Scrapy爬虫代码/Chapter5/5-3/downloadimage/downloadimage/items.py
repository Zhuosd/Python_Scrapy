# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DownloadimageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说名称
    title = scrapy.Field()
    # 小说作者
    author = scrapy.Field()
    # 小说类型
    type = scrapy.Field()
    # 图片URL
    image_urls = scrapy.Field()
    # 图片结果信息
    images = scrapy.Field()