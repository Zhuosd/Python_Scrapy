import requests

r = requests.get(url='http://www.bing.com')
print(r.content)
r = requests.post('http://httpbin.org/delete')
r = requests.put('http://httpbin.org/put', data={'key': 'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
