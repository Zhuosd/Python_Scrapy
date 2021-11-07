import scrapy

class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            # 传递表单数据
            formdata={'username': 'john', 'password': 'secret'},
            # 回调函数
            callback=self.after_login
        )

    def after_login(self, response):
        # 检查是否登录成功
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return
        # 执行登录通过后的操作
