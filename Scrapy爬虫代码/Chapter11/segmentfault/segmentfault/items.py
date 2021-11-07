# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SegmentfaultItem(scrapy.Item):
    # define the fields for your item here like:
    # 个人属性
    # 姓名
    name = scrapy.Field()
    # 声望
    rank = scrapy.Field()
    # 学校
    school = scrapy.Field()
    # 专业
    majors = scrapy.Field()
    # 公司
    company = scrapy.Field()
    # 工作
    job = scrapy.Field()
    # blog
    blog = scrapy.Field()
    # 社交活动数据
    # 关注人数
    following = scrapy.Field()
    # 粉丝数
    fans = scrapy.Field()
    # 回答数
    answers = scrapy.Field()
    # 提问数
    questions = scrapy.Field()
    # 文章数
    articles = scrapy.Field()
    # 讲座数
    lives = scrapy.Field()
    # 徽章数
    badges = scrapy.Field()
    # 技能属性
    # 点赞数
    like = scrapy.Field()
    # 技能
    skills = scrapy.Field()
    # 注册日期
    register_date = scrapy.Field()
    # 问答统计
    # 回答最高得票数
    answers_top_score = scrapy.Field()
    # 得票数最高的回答对应的问题的标题
    answers_top_title = scrapy.Field()
    # 得票数最高的回答对应的问题的标签
    answers_top_tags = scrapy.Field()
    # 得票数最高的回答对应的问题的内容
    answers_top_question = scrapy.Field()
    # 得票数最高的回答对应的问题的内容
    answers_top_content = scrapy.Field()





