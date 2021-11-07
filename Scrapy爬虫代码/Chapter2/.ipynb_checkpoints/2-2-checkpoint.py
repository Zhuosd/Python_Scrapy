import re

# 将正则表达式转化成Pattern对象
pattern = re.compile(r'(\d{4})-(\d{8})')
# 待匹配字符串
string1 = "0755-44445555 is our new office phone number"
string2 = "the old number 0755-11112222 is no longer used"
# 生成match对象
match1 = re.match(pattern, string1)
match2 = re.match(pattern, string2)

if match1:
    # re.match结果类型
    print(type(match1))
    # groups返回所有匹配结果
    print(match1.groups())
    # group(0)为未分组的原始匹配对象
    print(match1.group(0))
    # group(1)为第一组对象，以此类推
    print(match1.group(1))
    print(match1.group(2))
else:
    print('match1未匹配到对象')

if match2:
    print(match2)
    # groups返回所有匹配结果
    print(match2.groups())
    # group(0)为未分组的原始匹配对象
    print(match2.group(0))
    # group(1)为第一组对象，以此类推
    print(match2.group(1))
    print(match2.group(2))
else:
    print('match2未匹配到对象')
