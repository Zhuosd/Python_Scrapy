import scrapy

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class ErrbackSpider(scrapy.Spider):
    name = "errback_example"
    start_urls = [
        "http://www.httpbin.org/",              	# 正常HTTP 200返回
        "http://www.httpbin.org/status/404",    	# 404 Not found error
        "http://www.httpbin.org/status/500",    	# 500服务器错误
        "http://www.httpbin.org:12345/",        	# 超时无响应错误
        "http://www.httphttpbinbin.org/",       	# DNS 错误
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse_httpbin,
                                    errback=self.errback_httpbin,
                                    dont_filter=True)

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))
        # 其他处理.

    def errback_httpbin(self, failure):
        # 日志记录所有的异常信息
        self.logger.error(repr(failure))

        # 假设我们需要对指定的异常类型做处理，
        # 我们需要判断异常的类型

        if failure.check(HttpError):
            # HttpError由HttpErrorMiddleware中间件抛出
            # 可以接收到非200 状态码的Response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # 此异常由请求Request抛出
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

