# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest

class LoginwithcookieSpider(scrapy.Spider):
    name = 'loginwithcookie'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    cookies = {
		'__yadk_uid':'r1ui3ZQLIms2rcKxGyeNwLmzc8lUPH63',
		'_pk_id.100001.8cb4':'b74b50748759cfae.1548945951.5.1552140943.1549757800.',
		'_pk_ses.100001.8cb4':'*',
		'_vwo_uuid_v2':'D64CD4759E8B751D295BF6BB8C0A17D49|9bc14c89ac7c1fa5caf93699bc6283e7',
		'bid':'XzwxkKpWlcU',
		'dbcl2':'"190816154:EUPQ9myKid0"',
		'douban-profile-remind':'1',
		'gr_user_id':'7a61a89a-323b-45ca-9218-5029810ba568',
		'll':'"118282"',
		'push_doumail_num':'0',
		'push_noty_num':'0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language':	'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'book.douban.com',
        'Referer': 'https://www.douban.com/people/sugermaster/',
        'Upgrade-Insecure-Requests': '1',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"

}

    # 使用FormRequests发送请求，指定url，请求头信息，cookies
    def start_requests(self):
        for url in self.start_urls:
            return [FormRequest(url,
                                headers=self.headers,
                                # formdata={'name': '1120844583@qq.com',
                                #           'password': 'guoqing1010',
                                #           'remember': 'false'},
                                cookies=self.cookies,
                                callback=self.parse)]

    # 爬虫处理函数
    def parse(self, response):
        user_check = response.css(
            '.nav-user-account > a > span::text').extract_first()
        self.logger.info('{}已经登录成功'.format(user_check))