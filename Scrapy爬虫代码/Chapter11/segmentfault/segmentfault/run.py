from scrapy import cmdline
from segmentfault.get_cookies import GetCookies

if __name__ == '__main__':
    cookies = GetCookies()
    cookies.save()
    name = 'userinfo'
    ""
    cmd = 'scrapy crawl {}'.format(name)
    cmdline.execute(cmd.split())


