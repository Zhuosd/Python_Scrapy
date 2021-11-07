import scrapy


class TestSpider(scrapy.Spider):
    name = 'testspier'
    start_urls = ['http://www.bing.com']

    def parse(self, response):
        title = response.css('title: : text').extract_first()
        return({'title': title})
