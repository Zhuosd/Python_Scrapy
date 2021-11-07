# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http import FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/']

    # 请求头信息，豆瓣会禁止Scrapy默认的头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # 使用FormRequests发送请求，指定URL、请求头信息、请求参数、回调函数
    def start_requests(self):
        return [FormRequest(url='https://accounts.douban.com/j/mobile/login/basic',
                            headers=self.headers,
                            # 表单数据
                            formdata={'name': '1120844583@qq.com',
                                      'password': 'guoqing110',
                                      'remember': 'false'},
                            # 回调函数
                            callback=self.login_check)]

    # 检查登录状态，登录成功后回调爬虫处理函数
    def login_check(self, response):
        if "failed" not in response.text:
            # 登录成功，请求start_url中url
            for url in self.start_urls:
                yield scrapy.Request(url=url,
                                     headers=self.headers,
                                     callback=self.parse)
        else:
            # 登录失败，则提取失败描述信息
            data = json.loads(response.text)
            self.logger.info(data['description'])

    # 爬虫处理函数
    def parse(self, response):
        user_check = response.css('.nav-user-account > a > span::text').extract_first()
        self.logger.info('{}已经登录成功'.format(user_check))
