def parse_page1(self, response):
    item = MyItem()
    item['name'] = response.css('.name::text').extract_first()
    request = scrapy.Request("http://www.example.com/some_page.html",
                             callback=self.parse_page2)
    request.meta['item'] = item
    yield request

def parse_page2(self, response):
    item = response.meta['item']
    item['age'] = response.css('.age::text').extract_first()
    yield item
