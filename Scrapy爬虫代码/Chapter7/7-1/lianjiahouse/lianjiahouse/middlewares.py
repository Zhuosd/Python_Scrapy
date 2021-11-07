# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import scrapy
import random


class LianjiaSpiderMiddleware(object):
    """
    利用Scrapy数据收集功能，记录相同小区的数量
    """
    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        return cls(stats=crawler.stats)

    def process_spider_output(self, response, result, spider):
        """
        从item中获取小区名称，在数据收集其中记录相同小区数量
        :param response:
        :param result:
        :param spider:
        :return:
        """
        for item in result:
            if isinstance(item,scrapy.Item):
                # 从result中的item获取小区名称
                community_name = item['community_name']
                # 在数据统计中为相同的小区增加数量值
                self.stats.inc_value(community_name)
            yield item


class LianjiaDownloaderMiddleware(object):
    """
    为请求添加代理
    """
    def __init__(self,proxy_list):
        self.proxy_list = proxy_list

    @classmethod
    def from_crawler(cls, crawler):
        # 从settings.py中获取代理列表
        return cls(
            proxy_list=crawler.settings.get('PROXY_LIST')
        )

    def process_request(self, request, spider):
        # 从代理列表中随机选取一个添加至请求
        proxy = random.choice(self.proxy_list)
        request.meta['proxy'] = proxy

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)