import requests

payload = {
    'key1': 'value1',
    'key2': 'value2'
}
response = requests.post(url='http://www.bing.com', data=payload)
# json格式请求数据
# response = requests.post(url='http://www.bing.com', json=payload)
