from socket import *
import os



# 地址
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
namelist = {}


# 发送消息
def do_request(s):

    while True:
        data,addr = s.recvfrom(1024)
        msg = data.decode().split(' ')
        if msg[0] == 'L':
            print("name: ", data.decode())
            login(msg[1],addr,s)
        elif msg[0] == 'C':
            text=' '.join(msg[2:])
            do_chat(s,msg[1],text)
        elif msg[0] =='Q':
            if msg[1] not in namelist:
                s.sento(b'EXIT',addr)
                continue

            do_quit(s,msg[1])

def do_quit(s,name):
    msg='%s退出了聊天室'%name
    for i in namelist:
        if i !=name:
            s.sendto(msg.encode(),namelist[i])
        else:
            s.sendto(b'EXIT',namelist[i])
    try:
        del namelist[name]
    except:
        print('error')


def login(name,addr,s):
    if name in namelist:
        s.sendto(b'already exist', addr)
        return

    else:
        note= '当前有%s人 '% len(namelist)
        s.sendto(b'OK', addr)
        s.sendto(note.encode(), addr)
        msgg = "%s 进入聊天室" % name
        for i in namelist:
            s.sendto(note.encode(),addr)
            s.sendto(msgg.encode(), namelist[i])


        namelist[name] = addr

def do_chat(s, name, text):
    msg = "%s :%s"%(name,text)
    for i in namelist:
        if i !=name:
            s.sendto(msg.encode(),namelist[i])



def main():
    # 创建套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        return
    # 发送管理员消息
    elif pid == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员消息 " + msg
            s.sendto(msg.encode(), ADDR)
    else:
        # 请求处理
        do_request(s)  # 处理客户端请求






if __name__ =="__main__":
    main()
