# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lianjiahouse.items import LianjiahouseItem


class HouseSpider(CrawlSpider):
    name = 'house'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']

    rules = (
        Rule(LinkExtractor(allow='/ershoufang/\d{12}.html'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = LianjiahouseItem()
        # 二手房名称
        i['house_name'] = response.css('title::text').extract_first().replace(' ','')
        # 所在小区
        i['community_name'] = response.css('.communityName a::text').extract_first()
        # i['location'] = response.css()
        # 链家编号
        i['house_record'] = response.css('.houseRecord .info::text').extract_first()
        # 总价
        i['total_amount'] = response.css('.overview .total::text').extract_first()
        # 房屋信息
        # 单价
        i['unit_price'] = response.css('.unitPriceValue::text').extract_first()
        # 建筑总面积
        i['area_total'] = response.xpath('//div[@class="base"]//ul/li[3]/text()')\
            .re_first('\d+.\d+')
        # 使用面积
        i['area_use'] = response.xpath('//div[@class="base"]//ul/li[5]/text()')\
            .re_first('\d+.\d+')
        # 房屋类型
        i['house_type'] = response.xpath('//div[@class="base"]//ul/li[1]/text()')\
            .extract_first()
        # 房屋朝向
        i['direction'] = response.xpath('//div[@class="base"]//ul/li[7]/text()')\
            .extract_first()
        # 装修情况
        i['sub_info'] = response.xpath('//div[@class="base"]//ul/li[9]/text()')\
            .extract_first()
        # 供暖方式
        i['heating_method'] = response.xpath('//div[@class="base"]//ul/li[11]/text()')\
            .extract_first()
        # 产权
        i['house_property'] = response.xpath('//div[@class="base"]//ul/li[13]/text()')\
            .extract_first()
        # 楼层
        i['floor'] = response.xpath('//div[@class="base"]//ul/li[2]/text()')\
            .extract_first()
        # 总楼层
        i['total_floors'] = response.xpath('//div[@class="base"]//ul/li[2]/text()')\
            .re_first(r'\d+')
        # 是否有电梯
        i['is_left'] = response.xpath('//div[@class="base"]//ul/li[12]/text()')\
            .extract_first()
        # 户梯比例
        i['left_rate'] = response.xpath('//div[@class="base"]//ul/li[10]/text()')\
            .extract_first()
        # 挂牌时间
        i['release_date'] = response.xpath('//div[@class="transaction"]//ul/li[1]'
                                           '/span[2]/text()').extract_first()
        # 最后交易时间
        i['last_trade_time'] = response.xpath('//div[@class="transaction"]//ul/li[3]'
                                              '/span[2]/text()').extract_first()
        # 房屋使用年限
        i['house_years'] = response.xpath('//div[@class="transaction"]//ul/li[5]'
                                          '/span[2]/text()').extract_first()
        # 房屋抵押信息,抵押信息中有空格及换行符，先通过replace()将空格去掉，再通过strip()将换行符去掉
        i['pawn'] = response.xpath('//div[@class="transaction"]//ul/li[7]/span[2]'
                                   '/text()').extract_first().replace(' ','').strip()
        # 交易权属
        i['trade_property'] = response.xpath('//div[@class="transaction"]//ul/li[2]'
                                             '/span[2]/text()').extract_first()
        # 房屋用途
        i['house_usage'] = response.xpath('//div[@class="transaction"]//ul/li[4]'
                                          '/span[2]/text()').extract_first()
        # 产权所有
        i['property_own'] = response.xpath('//div[@class="transaction"]//ul/li[6]'
                                           '/span[2]/text()').extract_first()
        # 图片url
        i['images_urls'] = response.css('.smallpic > li::attr(data-pic)').extract()
        yield i
