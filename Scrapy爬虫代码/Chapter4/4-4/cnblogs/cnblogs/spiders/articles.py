from scrapy.spiders import SitemapSpider
from cnblogs.items import CnblogsItem

class MySpider(SitemapSpider):
    name = 'articles'
    # Sitemap 地址
    sitemap_urls = ['http://www.cnblogs.com/sitemap.xml']
    # 从Sitemap中提取url的规则，并指定回调方法
    sitemap_rules = [
        # 抓取 ***/cate/python/**的url，调用parse_python处理
        ('/cate/python/','parse_python')
    ]

    # 回调方法
    def parse_python(self,response):
        articles = response.css('.post_item')

        for article in articles:
            item = CnblogsItem()
            # 文章标题
            item['title'] = article.css('.titlelnk::text').extract_first()
            # 文章url
            item['url'] = article.css('.titlelnk::attr(href)').extract_first()
            # 文章作者
            item['author'] = article.css('.lightblue::text').extract_first()
            yield item
