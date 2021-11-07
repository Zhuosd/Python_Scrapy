# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IthomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 文章标题
    title = scrapy.Field()
    # 文章URL
    url = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 来源URL
    source_url = scrapy.Field()
    # 发布日期
    release_date = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 关键词
    key_words = scrapy.Field()

