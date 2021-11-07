import re

# 将正则表达式转化成Pattern对象
pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')
strings = 'Today is 2018-12-12, the date of the meeting is set at 2019-09-10, please confirm whether to participate before 2018-12-25'

# 定义日期格式转换方法，将'-'用'.'代替


def totype(match):
    return match.group(0).replace(r'-', '.')


new_strings = re.sub(pattern, totype, strings)

print(new_strings)
