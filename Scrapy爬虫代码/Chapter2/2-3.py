import re

# 将正则表达式转化成Pattern对象
pattern = re.compile(r'(\d{4})-(\d{8})')
# 待匹配字符串
string1 = "0755-44445555 is our new office phone number"
string2 = "the old number 0755-11112222 is no longer used"
#生成search对象
search1 = re.search(pattern, string1)
search2 = re.search(pattern, string2)

if search1:
    # re.search结果类型
    print('search1返回结果类型为:', type(search1))
    # groups返回所有匹配结果
    print('search1中groups的内容为:', search1.groups())
    # group(0)为未分组的原始匹配对象
    print('search1中group(0)的内容为:', search1.group(0))
    # group(1)为第一组对象，以此类推
    print('search1中group(1)的内容为:', search1.group(1))
    print('search1中group(2)的内容为:', search1.group(2))
else:
    print('search1未匹配到对象')

if search2:
    print('search2返回结果类型为:', type(search1))
    # groups返回所有匹配结果
    print('re.search返回结果类型为:', search2.groups())
    # group(0)为未分组的原始匹配对象
    print('search2中groups的内容为:', search2.group(0))
    # group(1)为第一组对象，以此类推
    print('search2中group(0)的内容为:', search2.group(0))
    print('search2中group(1)的内容为:', search2.group(1))
    print('search2中group(2)的内容为:', search2.group(2))
else:
    print('search2未匹配到对象')
