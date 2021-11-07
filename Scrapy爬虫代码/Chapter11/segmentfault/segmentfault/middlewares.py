# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import re
import datetime
import scrapy
import logging
import time
from scrapy.conf import settings
from pymongo import MongoClient
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
import pymongo
logger = logging.getLogger(__name__)


class SegmentfaultSpiderMiddleware(object):
    """
    处理Item中保存的三种类型注册日期数据：
    1. 注册于 2015年12月12日
    2. 注册于 3 天前
    3. 注册于 5 小时前
    """

    def process_spider_output(self,response,result,spider):

        """
        输出response时调用此方法处理item中register_date
        :param response:
        :param result: 包含item
        :param spider:
        :return:处理过注册日期的item
        """
        for item in result:
            # 判断获取的数据是否是scrapy.item类型
            if isinstance(item,scrapy.Item):
                # 获取当前时间
                now = datetime.datetime.now()
                register_date = item['register_date']
                logger.info("获取注册日志格式为{}".format(register_date))
                # 提取注册日期字符串，如'注册于2015年12月12日' => '20151212'
                day = ''.join(re.findall(r'\d+',register_date))
                # 如果提取数字字符串长度大于4位，则为'注册于2015年12月12日'形式
                if len(day) > 4:
                    date = day
                # 如果‘时’在提取的字符串中，则为'注册于8小时前'形式
                elif '时' in register_date:
                    d = now - datetime.timedelta(hours=int(day))
                    date = d.strftime("%Y%m%d")
                # 最后一种情况就是'注册于3天前'形式
                else:
                    d = now - datetime.timedelta(days=int(day))
                    date = d.strftime("%Y%m%d")

                # 更新register_date值
                item['register_date'] = date
            yield item


class SegmentfaultHttpProxyMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self):
        self.proxy_list = settings['PROXY_LIST']

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy_list)
        logger.info('使用代理:{}'.format(proxy))
        request.meta['proxy'] = proxy


class SegmentfaultUserAgentMiddleware(object):
    def __init__(self):
        self.useragent_list = settings['USER_AGENT_LIST']

    def process_request(self,request,spider):
        user_agent = random.choice(self.useragent_list)

        # logger.info('使用的USE USER-AGENT:{}'.format(user_agent))
        request.headers['User-Agent'] = user_agent



class SegmentfaultCookiesMiddleware(object):
    client = MongoClient(settings['MONGO_URI'])
    db = client[settings['MONGO_DB']]
    collection = db['cookies']

    def get_cookies(self):
        """
        随机获取cookies
        :return:
        """
        cookies = random.choice([cookie for cookie in self.collection.find()])
        # 将不需要的"_id"与"_gat"参数删除
        cookies.pop('_id')
        cookies.pop('_gat')
        # 将"Hm_lpvt_e23800c454aa573c0ccb16b52665ac26"填充当前时间
        cookies['Hm_lpvt_e23800c454aa573c0ccb16b52665ac26'] = str(int(time.time()))
        return cookies

    def remove_cookies(self,cookies):
        """
        删除已失效的cookies
        :param cookies:
        :return:
        """
        # 随机获取cookies中的一对键值,返回结果是一个元祖
        i = cookies.popitem()
        # 删除cookies
        try:
            logger.info("删除cookies{}".format(cookies))
            self.collection.remove({i[0]:i[1]})
        except Exception as e:
            logger.info("No this cookies:{}".format(cookies))

    def process_request(self,request,spider):
        """
        为每一个request添加一个cookie
        :param request:
        :param spider:
        :return:
        """
        cookies = self.get_cookies()
        request.cookies = cookies

    def process_response(self,request,response,spider):
        """
        对于登录失效的情况，可能会重定向到登录页面，这时添加新的cookies继续，将请求放回调度器
        :param request:
        :param response:
        :param spider:
        :return:
        """
        if response.status in [301,302]:
            logger.info("Redirect response:{}".format(response))
            redirect_url = response.headers['location']
            if b'/user/login' in redirect_url:
                logger.info("Cookies失效")

                # 请求失败，重新获取一个cookie，添加到request，并停止后续中间件处理此request，将此request放入调度器
                new_cookie = self.get_cookies()
                logger.info("获取新cookie:{}".format(new_cookie))
                # 删除旧cookies
                self.remove_cookies(request.cookies)
                request.cookies = new_cookie
            return request
        #
        return response





