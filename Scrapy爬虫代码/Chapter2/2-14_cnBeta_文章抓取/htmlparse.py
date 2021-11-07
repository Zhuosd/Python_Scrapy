from bs4 import BeautifulSoup
from datasave import DataSave
import re
import requests

class HtmlParse:
    # 主输出方法，返回提取的url列表与待保存的数据
    def parse_data(self,page_url,data):
        print("开始分析提取数据")
        # 如果待分析的文章的url或者数据为空，则不作处理
        if page_url is None or data is None:
            return
        soup =  BeautifulSoup(data,'lxml')
        urls = self.get_urls(soup)
        data = self.get_data(page_url,soup)
        return urls,data

    # 提取科技类文章url
    def get_urls(self,soup):
        urls = list()
        # 获取科技类文章地址tag
        links = soup.select('a[href*="/tech/"]')
        for link in links:
            # 从tag中提取网址数据
            url = link['href']
            urls.append(url)
        return urls

    # 提取文章数据
    def get_data(self,page_url,soup):
        data = {}
        # 将文章的地址，标题，发布日期保存到字典中
        # 文章url只是使用参数url
        data['url'] = page_url 
        # select_one获取符合条件的第一条
        # 获取文章标题
        title = soup.select_one('.cnbeta-article > header > h1')
        # 获取发布日期
        release_date = soup.select_one('.cnbeta-article > header > .meta > span')
        # 将数据保存到一个字典变量中
        data['title'] = title.get_text()
        data['release_date'] = release_date.get_text()
        print("文章url：{0}".format(page_url))
        print("数据：{0}".format(data))
        return data


if __name__ == "__main__":
    url = 'https://www.cnbeta.com/articles/tech/811395.htm'
    save = DataSave('D:\\Scrapy\\cnbeta.txt')
    response = requests.get(url)
    response.encoding = 'utf-8'
    parse = HtmlParse()
    u,d = parse.parse_data(url,response.text)
    save.save(d)
    print(u,d)


    
