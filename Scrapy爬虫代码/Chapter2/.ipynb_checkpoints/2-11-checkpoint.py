import requests

payload = {
    'q': 'requests',
    'qs': 'HS',
    'pq': 'requests',
    'sc': '8-8',
    'cvid': '3FF015B95B824F98B6E0C0105EA6BD7C',
    'from': 'QBLH',
    'sp': 1}
response = requests.get(url='http://www.bing.com', params=payload)
print(response.request.url)