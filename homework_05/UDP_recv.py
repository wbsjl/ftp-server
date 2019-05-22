from socket import *
import struct


#创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8888))

while True:
    data,addr = sockfd.recvfrom(1024)
    i=struct.unpack('i4sif',data)
    print("Recived: ", i)
    st="%d  %s %d %f\n"%(i[0],i[1].decode(),i[2],i[3])
    new_one = open('test','a')
    new_one.write(st)
    sockfd.sendto(b'Thanks', addr)
new_one.close()
sockfd.close()