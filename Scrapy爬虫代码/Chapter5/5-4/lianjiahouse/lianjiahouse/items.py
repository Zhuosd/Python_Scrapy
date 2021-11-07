# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiahouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 发布信息名称
    house_name = scrapy.Field()
    # 小区名称
    community_name = scrapy.Field()
    # 所在区域
    # location = scrapy.Field()
    # 链家编号
    house_record = scrapy.Field()
    # 总售价
    total_amount = scrapy.Field()
    # 单价
    unit_price = scrapy.Field()
    # 房屋基本信息
    # 建筑面积
    area_total = scrapy.Field()
    # 套内面积
    area_use = scrapy.Field()
    # 厅室户型
    house_type = scrapy.Field()
    # 朝向
    direction = scrapy.Field()
    # 装修情况
    sub_info = scrapy.Field()
    # 供暖方式
    heating_method = scrapy.Field()
    # 产权
    house_property = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 总层高
    total_floors = scrapy.Field()
    # 电梯
    is_left = scrapy.Field()
    # 户梯比例
    left_rate = scrapy.Field()
    # 户型结构
    structure = scrapy.Field()
    # 房屋交易信息
    # 挂牌时间
    release_date = scrapy.Field()
    # 上次交易时间
    last_trade_time = scrapy.Field()
    # 房屋使用年限
    house_years = scrapy.Field()
    # 房屋抵押信息
    pawn = scrapy.Field()
    # 交易权属
    trade_property = scrapy.Field()
    # 房屋用途
    house_usage = scrapy.Field()
    # 产权所有
    property_own = scrapy.Field()
    # 图片地址
    images_urls = scrapy.Field()
    # 保存图片
    images = scrapy.Field()
