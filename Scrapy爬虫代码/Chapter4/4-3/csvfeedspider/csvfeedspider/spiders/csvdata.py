# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from csvfeedspider.items import CsvspiderItem


class CsvparseSpider(CSVFeedSpider):
    name = 'csvdata'
    allowed_domains = ['gzdata.gov.cn']
    start_urls = ['http://gzopen.oss-cn-guizhou-a.aliyuncs.com/科技特派员.csv']
    headers = ['name', 'SearchField', 'Service', 'Specialty']
    delimiter = ','
    quotechar = "\n"

    # Do any adaptations you need here
    def adapt_response(self, response):
       return response.body.decode('gb18030')

    def parse_row(self, response, row):

        i = CsvspiderItem()
        try:
            i['name'] = row['name']
            i['SearchField'] = row['SearchField']
            i['Service'] = row['Service']
            i['Specialty'] = row['Specialty']

        except:
            pass
        yield i
