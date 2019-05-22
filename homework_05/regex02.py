import re

pattern = r'(ab)cd(?P<biu>ef)'
regex = re.compile(pattern)
obj = regex.search('abcdefghijk',pos=0,endpos=11)
print(regex.groupindex)
print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)
print('=========================')


print(obj.start())
print(obj.end())
print(obj.span())
print(obj.groups())
print(obj.group(1,'biu',1 ))
print(obj.groupdict())
