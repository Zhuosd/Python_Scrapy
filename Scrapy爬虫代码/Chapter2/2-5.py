import re

# 将正则表达式转化成Pattern对象
pattern = re.compile(r'\W')
# 待匹配字符串
strings = 'This$is&the@largest%ball'

result = re.split(pattern, strings)

print(result)
