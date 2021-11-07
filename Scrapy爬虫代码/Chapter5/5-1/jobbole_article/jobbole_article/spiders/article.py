# -*- coding: utf-8 -*-
import scrapy
from jobbole_article.items import JobboleArticleItem


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        all_post = response.css(".post")
        for post in all_post:
            item = JobboleArticleItem()
            item['title'] = post.css('.archive-title::text').extract_first()
            item['summary'] = post.css('.excerpt p::text').extract_first()
            # 根据正则表达式提取发表日期
            item['publish_date'] = post.css('.post-meta p::text').re_first(r'\d{4}/\d{2}/\d{2}')
            # Tag 标签可能有多个，因此不需要获取第一个值，保存列表即可
            item['tag'] = post.xpath(".//a[2]/text()").extract()
            yield item

        # 检查是否有下一页url,如果有下一页则调用parse进行处理
        next_page = response.css('.next::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(next_page,callback=self.parse)
