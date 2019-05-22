# i=open("test",'r+')
# print(i.read())
# print(i.readline(-1))
# print(i.readlines(1))
with open('test','r+') as i:
    for line in i:
        print(line)
    print(i.tell())
    i.writelines("hihi")
    i.seek(5,0)
    print(i.tell())
    print(i.read(10))
    i.flush()