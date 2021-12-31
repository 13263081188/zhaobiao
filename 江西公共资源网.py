import re
str1="pdasssy</\\\"\n=\\'hhh"
pat="y</.\"\n=\.h"
# rst = re.match(pat,str1)
rst = re.compile(pat).findall(str1)
print(rst[0])
# help(rst)
# print(type(rst))

#match从头开始匹配，头部不满足就不满足；
#search 从非头开始匹配，但只能输出一个匹配