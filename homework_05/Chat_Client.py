"""
group chat
python3.5

"""

from socket import *
import os ,sys
sockfd = socket(AF_INET, SOCK_DGRAM)
# 服务器地址
HOST = '176.122.17.93'
PORT = 8888
ADDR = (HOST,PORT)

def send(s):
    while True:
        name = input("Name >>")
        msg = "L "+name
        if msg == "L ":
            break
        s.sendto(msg.encode(),ADDR)
        resp,addr = s.recvfrom(1024)
        print("from server:",resp.decode())
        if resp.decode() == 'OK':
            break


    pid = os.fork()
    if pid<0:
        sys.exit('error')
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s,name)

def send_msg(s,name):
    while True:
        text = input("说：")
        if text == 'quit':
            msg = "Q "+ name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")


        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s,name):
    while True:
        data, addr = s.recvfrom(2048)
        print(data.decode())



def main():
    s = socket(AF_INET, SOCK_DGRAM)
    send(s)
    # name = input('name')
    # s.sendto(name.encode(),ADDR)
    s.close()

if __name__ =="__main__":
    main()
