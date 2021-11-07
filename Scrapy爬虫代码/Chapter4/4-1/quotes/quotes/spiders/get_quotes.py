import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Quotes(CrawlSpider):
	# 爬虫名称
    name = "get_quotes"
    allow_domain = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

# 设定规则
    rules = (
        # 对于quotes内容页URL，调用parse_quotes处理，
      		# 并以此规则跟进获取的链接
        Rule(LinkExtractor(allow=r'/page/\d+'), callback='parse_quotes', follow=True),
      		# 对于author内容页URL，调用parse_author处理，提取数据
        Rule(LinkExtractor(allow=r'/author/\w+'), callback='parse_author')
    )

# 提取内容页数据方法
    def parse_quotes(self, response):
        for quote in response.css(".quote"):
            yield {'content': quote.css('.text::text').extract_first(),
                   'author': quote.css('.author::text').extract_first(),
                   'tags': quote.css('.tag::text').extract()
                   }
	# 获取作者数据方法

    def parse_author(self, response):
        name = response.css('.author-title::text').extract_first()
        author_born_date = response.css('.author-born-date::text').extract_first()
        author_bron_location = response.css('.author-born-location::text').extract_first()
        author_description = response.css('.author-description::text').extract_first()

        return ({'name': name,
                 'author_bron_date': author_born_date,
                 'author_bron_location': author_bron_location,
                 'author_description': author_description
                 })
