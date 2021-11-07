# -*- coding: utf-8 -*-
import scrapy
from downloadfile.items import DownloadfileItem


class GetfileSpider(scrapy.Spider):
    name = 'getfile'
    allowed_domains = ['szhrss.gov.cn']
    start_urls = ['http://hrss.sz.gov.cn/wsbs/xzzx/rcyj/']

    def parse(self, response):
        files_list = response.css('.conRight_text_ul1 li')
        for file in files_list:
            item = DownloadfileItem()
            item['file_name'] = file.css('a::text').extract_first()
            item['release_date'] = file.css('span::text').extract_first()
            # 由于获取到的url类似"./201501/P020170328745500534334.doc"
            # 所以需要手动调整为完成的url格式
            url = file.css('a::attr(href)').extract_first()
            # file_urls必须是list形式
            item['file_urls'] = [response.url + url[1:]]
            yield item
