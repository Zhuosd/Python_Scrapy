# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy import Request
from pymongo import MongoClient
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import FormRequest
from segmentfault.items import SegmentfaultItem


class UserinfoSpider(CrawlSpider):
    name = 'userinfo'
    allowed_domains = ['segmentfault.com']
    start_urls = ['https://segmentfault.com/u/mybigbigcat/users/following']

    rules = (
        # 用户主页地址，跟进并进行解析
        Rule(LinkExtractor(allow=r'/u/\w+$'),callback='parse_item',follow=True),
        # 用户关注列表，跟进列表页面，抓取用户主页地址进行后续操作
        # Rule(LinkExtractor(allow=r'/users/followed$'),follow=True),
        # 用户粉丝列表，跟进列表页面，抓取用户主页地址进行后续操作
        Rule(LinkExtractor(allow=r'/users/following$'),follow=True),
        # 跟进其他页面地址
        # Rule(LinkExtractor(allow=r'/users/[followed|following]?page=\d+'),follow=True),
    )

    def start_requests(self):
        # 从MongoDB中获取一条cookie，添加到开始方法
        client = MongoClient(self.crawler.settings['MONGO_URI'])
        db = client[self.crawler.settings['MONGO_DB']]
        cookies_collection = db.cookies
        # 获取一条cookie
        cookies = cookies_collection.find_one()
        # cookie中的'Hm_lpvt_e23800c454aa573c0ccb16b52665ac26'参数是当前时间的10位表示法，因此重新填充
        cookies['Hm_lpvt_e23800c454aa573c0ccb16b52665ac26'] = str(int(time.time()))

        return [Request("https://segmentfault.com",
                        cookies=cookies,
                        meta={'cookiejar':1},
                        callback=self.after_login)]

    # 登录之后从start_url中开始抓取数据
    def after_login(self,response):
        for url in self.start_urls:
            return self.make_requests_from_url(url)
    # def after_login(self,response):
    #     yield Request(self.start_urls[0],
    #                    meta={'cookiejar':response.meta['cookiejar']},
    #                    callback=self.parse_item)

    def parse_item(self, response):
        """
        :param response:
        :return:
        """
        item = SegmentfaultItem()
        # 个人属性模块
        profile_head = response.css('.profile__heading')
        # 姓名
        item['name'] = profile_head.css('h2[class*=name]::text').re_first(r'\w+')
        # 声望
        item['rank'] = profile_head.css('.profile__rank-btn > span::text').extract_first()
        # 学校专业信息
        school_info = profile_head.css('.profile__school::text').extract()
        if school_info:
            # 学校
            item['school'] = school_info[0]
            # 专业
            item['majors'] = school_info[1].strip()
        else:
            item['school'] = ''
            item['majors'] = ''
        # 公司职位信息
        company_info = profile_head.css('.profile__company::text').extract()
        if company_info:
            # 公司
            item['company'] = company_info[0]
            # 职位
            item['job'] = company_info[1].strip()
        else:
            item['company'] = ''
            item['job'] = ''
        # 个人博客
        item['blog'] = profile_head.css('a[class*=other-item-link]::attr(href)').extract_first()

        # 统计面板模块
        profile_active = response.xpath("//div[@class='col-md-2']")
        # 关注人数
        item['following'] = profile_active.css('div[class*=info] a > .h5::text').re(r'\d+')[0]
        # 粉丝人数
        item['fans'] = profile_active.css('div[class*=info] a > .h5::text').re(r'\d+')[1]
        # 回答问题数
        item['answers'] = profile_active.css('a[href*=answer] .count::text').re_first(r'\d+')
        # 提问数
        item['questions'] = profile_active.css('a[href*=questions] .count::text').re_first(r'\d+')
        # 文章数
        item['articles'] = profile_active.css('a[href*=articles] .count::text').re_first(r'\d+')
        # 讲座数
        item['lives'] = profile_active.css('a[href*=lives] .count::text').re_first(r'\d+')
        # 徽章数
        item['badges'] = profile_active.css('a[href*=badges] .count::text').re_first(r'\d+')
        # 徽章详细页面地址
        badge_url = profile_active.css('a[href*=badges]::attr(href)').extract_first()

        # 技能面板模块
        profile_skill = response.xpath("//div[@class='col-md-3']")
        # 技能标签列表
        item['skills'] = profile_skill.css('.tag::text').re(r'\w+')
        # 获得的点赞数
        item['like'] = profile_skill.css('.authlist').re_first(r'获得 (\d+) 次点赞')
        # 注册日期
        item['register_date'] = profile_skill.css('.profile__skill--other p::text').extract_first()
        # if register_time:
        #     item['register_date'] = ''.join(re.findall(r'\d+',register_time))
        # else:
        #     item['register_date'] = ''

        # 产出数据模块
        profile_work = response.xpath("//div[@class='col-md-7']")
        # 回答获得的最高分
        item['answers_top_score'] = profile_work.css('#navAnswer .label::text').re_first(r'\d+')
        # 最高分回答对应的问题的标题
        item['answers_top_title'] = profile_work.css('#navAnswer div[class*=title-warp] > a::text').extract_first()
        # 最高分回答对应的问题的url
        answer_url = profile_work.css('#navAnswer div[class*=title-warp] > a::attr(href)').extract_first()

        # 将需要继续跟进抓取数据的url与item作为参数传递给相应方法继续抓取数据
        request = scrapy.Request(
            # 问题详细页url
            url=response.urljoin(answer_url),
            meta={
            # item需要传递
            'item':item,
            # 徽章的url
            'badge_url':response.urljoin(badge_url)},
            # 调用parse_ansser继续处理
            callback=self.parse_answer)
        yield request

    def parse_answer(self,response):
        # 取出传递的item
        item = response.meta['item']
        # 取出传递的徽章详细页url
        badge_url = response.meta['badge_url']
        # 问题标签列表
        item['answers_top_tags'] = response.css('.question__title--tag .tag::text').re(r'\w+')
        # 先获取组成问题内容的字符串列表
        question_content = response.css('.widget-question__item p').re(r'>(.*?)<')
        # 拼接后传入item
        item['answers_top_question'] = ''.join(question_content)
        # 先获取组成答案的字符串列表
        answer_content = response.css('.qa-answer > article .answer').re(r'>(.*?)<')
        # 拼接后传入item
        item['answers_top_content'] = ''.join(answer_content)

        # 问题页面内容抓取后继续抓取徽章页内容，并将更新后的item继续传递
        request = scrapy.Request(url=badge_url,
                                 meta={'item':item},
                                 callback=self.parse_badge)
        yield request

    def parse_badge(self,response):
        item = response.meta['item']
        badge_name = response.css('span.badge span::text').extract()
        badge_count = response.css('span[class*=badges-count]::text').re(r'\d+')
        name_count = {}
        for i in range(len(badge_count)):
            name_count[badge_name[i]] = badge_count[i]
        item['badges'] = name_count
        yield item





