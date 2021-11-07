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
        return [scrapy.FormRequest(
            "http://www.example.com/login",
            # 传递表单数据
            formdata={'user': 'john', 'pass': 'secret'},
            # 回调函数
            callback=self.login_check)]

    # 检查是否登录成功
    def login_check(self, response):

        # 如果登录成功，则从start_url生成Request，调用parse_page进行解析
        if "Login failed" not in response.body:
            for url in self.start_urls:
                yield scrapy.Request(url, callback=self.parse_page)

    # 解析页面
    def parse_page(self, response):
        item = ExampleItem()
        item["name"] = response.css(".name").extract_first()
