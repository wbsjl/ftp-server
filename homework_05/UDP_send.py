from socket import *
import struct


sockfd = socket(AF_INET, SOCK_DGRAM)
# 服务器地址
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)
while True:
    id=int(input("id"))
    name=(input("name"))
    age=int(input("age"))
    grade = int(input("grade"))
    data = struct.pack('i4sif',id,name.encode(),age,grade)
    print(data)
    sockfd.sendto(data,ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("from server:",msg.decode())
sockfd.close()