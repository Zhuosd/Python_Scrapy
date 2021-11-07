import scrapy


class JobboleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 文章标题
    title = scrapy.Field()
    # 发表日期
    public_date = scrapy.Field()
    # 文章链接
    link = scrapy.Field()
