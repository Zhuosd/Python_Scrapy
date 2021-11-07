# -*- coding: utf-8 -*-
import scrapy
from downloadimage.items import DownloadimageItem


class GetimageSpider(scrapy.Spider):
    name = 'getimage'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/finish']

    def parse(self, response):
        for novel in response.css(".all-img-list > li"):
            item = DownloadimageItem()
            item['title'] = novel.xpath('.//h4/a/text()').extract_first()
            item['author'] = novel.css('.name::text').extract_first()
            item['type'] = novel.css('em + a::text').extract_first()
            item['image_urls'] = ['https:' + novel.xpath('.//img/@src').extract_first()]
            yield item
