# 使用Cookie
import http.cookiejar
import urllib.request
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('saved_cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
