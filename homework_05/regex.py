import re


# s = 'Levi: 1994, Sunny: 1993'
# pattern = r"(\w+)(:\s*\d+)"
# l = re.findall(pattern, s)
# print(l)
# regex = re.compile(pattern)
# l = regex.findall(s,0,7)
# print(l)
# s = 'hello world how are  . you'
# l = re.split(r'\W+',s)
# print(l)
# s = '时间: 2019/10/12'
# ns =re.subn(r'\d+','.',s)
# print(ns)
# s = r'2019,abu,70,year'
# pattern = r'\W'
# it = re.search(pattern,s)
# print(it.group())
# s = r'2019,abu,70,year'
# pattern = r'\d'
# it = re.match(pattern,s)
# print(it.group())

#
# s = r'2019,abu,70,year'
# pattern = r'.+'
# it = re.fullmatch(pattern,s)
# print(it.group())


s = 'Levi: 1994, Sunny: 1993'
pattern = r"(\w)(\d)"
regex = re.compile(pattern)
print(regex.groupindex)

