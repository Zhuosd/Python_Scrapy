# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsvspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 姓名
    name = scrapy.Field()
    # 研究领域
    SearchField = scrapy.Field()
    # 服务分类
    Service = scrapy.Field()
    # 专业特长
    Specialty = scrapy.Field()

