# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ithome.items import IthomeItem
import datetime


class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['ithome.com']
    start_urls = ['https://www.ithome.com/0/411/151.htm']

    rules = (
        # 文章URL形如：https://www.ithome.com/0/411/369.htm
        # 根据后三段数字来提取所有的文章url并跟进处理数据
        Rule(LinkExtractor(allow=r'/\d/\d{3}/\d{3}'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = IthomeItem()
        # 文章URL
        item['url'] = response.url
        # 文章标题
        item['title'] = response.css('.post_title > h1::text').extract_first()
        # 文章作者
        item['author'] = response.css('#author_baidu strong::text').extract_first()
        # 文章来源
        item['source'] = response.css('#source_baidu > a::text').extract_first()
        # 文章来源URL
        item['source_url'] = response.css('#source_baidu > a::attr(href)').extract_first()
        # 发布日期
        item['release_date'] = response.css('#pubtime_baidu::text').extract_first()
        # 关键词
        item['key_words'] = response.css('.hot_tags > span a::text').extract()
        return item

    def close(self,spider, reason):
        self.crawler.stats.set_value('finish_time',datetime.datetime.now())
