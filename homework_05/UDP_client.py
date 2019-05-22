from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)
# 服务器地址
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

while True:
    data = input("Msg >>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("from server:",msg.decode())

sockfd.close()