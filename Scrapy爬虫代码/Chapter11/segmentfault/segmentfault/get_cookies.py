from selenium import webdriver
from pymongo import MongoClient
from scrapy.crawler import overridden_settings
from segmentfault import settings
import time


class GetCookies(object):
    def __init__(self):
        # 初始化组件
        # 设定webdriver选项
        self.opt = webdriver.ChromeOptions()
        self.opt.add_argument("--headless")
        # 初始化用户列表
        self.user_list = settings.USER_LIST
        # 初始化MongoDB参数
        self.client = MongoClient(settings.MONGO_URI)
        self.db = self.client[settings.MONGO_DB]
        self.collection = self.db["cookies"]

    def get_cookies(self,username,password):
        """

        :param username:
        :param password:
        :return: cookies
        """
        # 使用webdriver选项创建driver
        driver = webdriver.Chrome(options=self.opt)
        driver.get("https://segmentfault.com/user/login")
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.get("https://segmentfault.com/u/luwangmeilun/users/following")
        # 登陆之后获取页面cookies
        cookies = driver.get_cookies()
        driver.quit()

        return cookies

    def format_cookies(self,cookies):
        """

        :param cookies:
        从driver.get_cookies的形式为：
        [{'domain': 'segmentfault.com', 'httpOnly': False, 'name': 'PHPSESSID',
        'path': '/', 'secure': False, 'value': 'web2~5grmfa89j12eksub8hja3bvaq4'},
        {'domain': '.segmentfault.com', 'expiry': 1581602940, 'httpOnly': False,
        'name': 'Hm_lvt_e23800c454aa573c0ccb16b52665ac26', 'path': '/', 'secure': False,
        'value': '1550066940'},
        {'domain': '.segmentfault.com', 'httpOnly': False,
        'name': 'Hm_lpvt_e23800c454aa573c0ccb16b52665ac26',
        'path': '/', 'secure': False, 'value': '1550066940'},
        {'domain': '.segmentfault.com', 'expiry': 1550067000, 'httpOnly': False,
        'name': '_gat', 'path': '/', 'secure': False, 'value': '1'},
        {'domain': '.segmentfault.com', 'expiry': 1550153340, 'httpOnly': False,
        'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.783265084.1550066940'},
        {'domain': '.segmentfault.com', 'expiry': 1613138940, 'httpOnly': False, 'name': '_ga',
        'path': '/', 'secure': False, 'value': 'GA1.2.1119166665.1550066940'}]
        只需提取每一项的name与value即可

        :return:
        """
        c = dict()
        for item in cookies:
            c[item['name']] = item['value']

        return c

    def save(self):
        print("开始获取Cookies....")
        # 从用户列表中获取用户名与密码，分别登陆获取cookies
        for username,password in self.user_list:
            cookies = self.get_cookies(username,password)
            f_cookies = self.format_cookies(cookies)
            print("insert cookie:{}".format(f_cookies))
            # 将格式整理后的cookies插入MongoDB数据库
            self.collection.insert_one(f_cookies)

        # s = db[self.collection].find()
        # for i in s:
        #     print(i)


if __name__ == '__main__':

    cookies = GetCookies()
    for i in range(20):
        cookies.save()
