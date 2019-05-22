fd = open("test","r+")


print("当前文件偏移量位置：",fd.tell())
print(fd.read(2))
print("当前文件偏移量位置：",fd.tell())
fd.seek(5,0)
print(fd.read(2))


fd.close()