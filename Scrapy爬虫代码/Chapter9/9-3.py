import scrapy

from myprojct.items import ExampleItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ["example.com"]

    start_urls = [
        'http://www.example.com',
    ]

    # 先登录
    def start_requests(self):
        # Cookies数据
        cookies = {'uid': '"1083428ut78j8"', 'v': '30'}
        # 头信息
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }

        return [scrapy.FormRequest("http://www.example.com/articles",
                                   # 使用Cookies
                                   cookies=cookies,
                                   # 指定头信息
                                   headers=headers,
                                   # 指定回调函数
                                   callback=self.parse_page)]


    # 解析页面
    def parse_page(self, response):
        item = ExampleItem()
        item["name"] = response.css(".name").extract_first()
        yield item
