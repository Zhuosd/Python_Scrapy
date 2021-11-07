from datasave import DataSave
from htmldownloader import HtmlDownloader
from htmlparse import HtmlParse
from urlmanager import URLManager

class Scheduler:
    def __init__(self,path,root_url,count):
        # 初始化各个组件
        self.url_manager = URLManager()
        self.data_save = DataSave(path)
        self.html_parser = HtmlParse()
        self.downloader = HtmlDownloader()
        self.root_url = root_url
        self.count = count

    def run_spider(self):
        # 先添加一条url到未爬取url集合中
        self.url_manager.save_new_url(self.root_url)
        # 判断：如果未爬取url集合中还有网址，并且还没有爬取到50篇文章，那么继续爬去
        while self.url_manager.get_new_url_num() and self.url_manager.get_old_url_num() < self.count:
            try:
                # 获取一条未爬取url
                url = self.url_manager.get_new_url()
                # 下载数据
                response = self.downloader.download(url)
                # 分析数据，返回url与文章相关数据
                new_urls,data = self.html_parser.parse_data(url,response)
                # 将获取到的url保存到未爬取url集合中
                self.url_manager.save_new_urls(new_urls)
                # 保存数据到本地文件
                self.data_save.save(data)
                print("已经抓取了{0}篇文章".format(len(self.url_manager.old_urls)))
            except Exception as e:
                print("本篇文章抓取停止,{0}".format(e))


if __name__ == "__main__":
    root_url = "https://www.cnbeta.com/articles/tech/812819.htm"
    save_url = "D:\\Scrapy\\chap2\\2-1\\cnbeta.txt"
    Spider = Scheduler(save_url,root_url,20)
    Spider.run_spider()


