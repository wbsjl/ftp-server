from socket import *


#创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8888))


data,addr = sockfd.recvfrom(5)
print("Recived: ", data.decode())
sockfd.sendto(b'Thanks', addr)

sockfd.close()
