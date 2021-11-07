import http.cookiejar
import urllib.request
# 保存Cookie
filename = 'saved_cookies.txt'
# FileCookieJar、MozillaCookieJar、LWPCookieJar约为保存cookie信息，
# 只是保存格式不同，读者可自行尝试
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
