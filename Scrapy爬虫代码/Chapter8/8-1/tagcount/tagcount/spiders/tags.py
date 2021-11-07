# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from tagcount.items import TagcountItem


class TagsSpider(scrapy.Spider):
    name = 'tags'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = TagcountItem()
            # 提取内容数据
            item['author'] = quote.css('.author::text').extract_first()
            item['content'] = quote.css('.text::text').extract_first()
            item['tag'] = quote.css('.tag::text').extract()
            if 'love' in item['tag']:
                # 如果“love”在获取的tag内容中，则“love”统计数量+1
                self.crawler.stats.inc_value('love')
            yield item

        next_page = response.css('.next > a::attr(href)').extract_first()
        if next_page is not None:
            yield Request(response.urljoin(next_page), callback=self.parse)
