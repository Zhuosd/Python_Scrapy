# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
# 导入item
from xmlfeedspider.items import JobboleItem


class JobboleSpider(XMLFeedSpider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://top.jobbole.com/feed/']
    iterator = 'iternodes'  # 迭代器，不指定的话默认是iternodes
    itertag = 'item'  # 抓取item节点

    def parse_node(self, response, selector):
        item = JobboleItem()
        item['title'] = selector.css('title::text').extract_first()
        item['public_date'] = selector.css('pubDate::text').extract_first()
        item['link'] = selector.css('link::text').extract_first()
        return item
