from selenium import webdriver
from bs4 import BeautifulSoup
import time


class Lagou:
    def __init__(self):
        # 定义浏览器驱动
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 起始网址
        self.url = "https://www.lagou.com/"

    def search(self, keywords):
        # 打开页面
        self.driver.get(self.url)
        # 关闭弹窗
        self.driver.find_element_by_xpath("//a[@class='tab focus']").click()

        # 搜索框中输入关键字
        self.driver.find_element_by_css_selector("#search_input").send_keys(keywords)
        # 点击按钮
        self.driver.find_element_by_xpath("//input[@id='search_button']").click()
        # 等待两秒
        time.sleep(2)
        # 获取页面html
        page_source = self.driver.page_source
        # 关闭浏览器
        self.driver.quit()

        return page_source

    def get_jobs(self, page_source):
        # 使用BeautifulSoup解析页面
        soup = BeautifulSoup(page_source, 'lxml')
        # 获取所有的招聘条目
        hot_items = soup.select('.con_list_item')
        for item in hot_items:
            d = dict()
            # 获取工作岗位名称
            d['job'] = item.select_one(".position_link > h3").get_text()
            # 获取公司名称
            d['company'] = item.select_one(".company_name > a").get_text()
            # 获取薪资
            d['salary'] = item.select_one(".money").get_text()
            print(d)


if __name__ == "__main__":
    hot = Lagou()
    # 搜索关键字
    page_source = hot.search('python')
    hot.get_jobs(page_source)
