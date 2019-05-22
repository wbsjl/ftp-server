import re

s = """Hello World
你好, 北京
~0_0~
0"""

regex = re.compile(r'\w+',flags=re.A)
l = regex.findall(s)
print(l)


regex = re.compile(r'~*[a-z]+~*',flags=re.I)
l = regex.findall(s)
print(l)

regex = re.compile(r'.*',flags=re.S)
l = regex.findall(s)
print(l)


regex = re.compile(r'^你好',flags=re.M)
l = regex.findall(s)
print(l)



pattern = r"""\w+ # yo 
# \s+ # yoyo 
# \w+ # yoyoyo 

"""
regex = re.compile(pattern,flags=re.X)
l = regex.findall(s)
print(l)

