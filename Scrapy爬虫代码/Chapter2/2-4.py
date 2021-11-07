import re

# 将正则表达式转化成Pattern对象
pattern = re.compile(r'\d+')
# 待匹配字符串
strings = 'Your activation code is 73829-72993-00983-84721'
result = re.findall(pattern, strings)

print(result)
