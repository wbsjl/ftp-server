from socket import *
from threading import Thread
import sys,signal,os
from time import sleep
s = socket()
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
checklist= []
FTP ='/home/tarena/FTP/'
print("listening the port 8888...")


class Request:
    def __init__(self,c,FTP_PATH):
        self.c = c
        self.path = FTP_PATH

    def dolist(self):
        files = os.listdir(self.path)
        if not files:
            self.c.send(b"empty")
            return
        else:
            self.c.send(b'  ')
            sleep(0.1)
        ff = ''
        for file in files:
            if file[0] is not'.'and os.path.isfile(self.path+file):
             ff += file+'\n'
        self.c.send(ff.encode())

    def dodownload(self,filename):
        try:
            fd=open(self.path+filename,'rb')
        except Exception as a:
            self.c.send('file search error'.encode())
            return
        else:
            self.c.send(b'open succesfully')
            sleep(0.1)
        while True:
            data = fd.read(1024)
            if not data:
                sleep(0.1)
                self.c.send(b'##')
                break
            self.c.send(data)
    def doupload(self,filename):
        try:
            fd=open(self.path+filename,'wb')
        except Exception as a:
            self.c.send('file open error'.encode())
            return
        else:
            self.c.send(b'ready')
            sleep(0.1)
        while True:
            data = self.c.recv(1024)
            print(data)
            if data == b'##':
                sleep(0.1)
                break
            fd.write(data)
        fd.close()
    # def handle(self,c,filename=''):
    #     print('客户端:',c.getpeername())
    #     while True:
    #
    #         data = c.recv(1024)
    #         if data.decode() == '1':
    #             Request.upload(self,c,filename)
    #         if not data:
    #             break
    #
    #         print(data.decode())
    #         c.send(b"uploaded")
    # def upload(self,c,filename):
    #     print('ｏｋ')
    #     f = open('/home/tarena/FTP/%s'%filename,'wb')
    #     data = c.recv(1024)
    #     # while True:
    #     #
    #     #     if not data:
    #     #         break
    #     f.write(data)
    #     c.send(b"uploaded")
    #     checklist.append(filename)




def handle(connfd):
    cls = connfd.recv(1024).decode()
    FTP_PATH = FTP + cls + '/'
    ftp=Request(connfd,FTP_PATH)
    print(FTP_PATH)
    while True:
        data = connfd.recv(1024).decode()
        print(data)
        if data[0]=='Q'or not data:
            return
        elif data[0] =='L':
            ftp.dolist()
        elif data[0] =='G':
            print(data.split(' '))
            i = data.split(' ')
            while i[-1]==" ":
                i.remove(i[-1])

            filename = i[-1]
            ftp.dodownload(filename)
        elif data[0] =='U':
            filename = data.split(' ')[-1]
            ftp.doupload(filename)


def main():

    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)
    # #处理僵尸
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    while True:
        try:

            c,addr = s.accept()
        except KeyboardInterrupt:
            sys.exit("退出")
        except Exception as e:
            print(e)
            continue
        print("链接的客户端：", addr)

        t = Thread(target =handle, args=(c,))
        t. setDaemon(True)
        t.start()

if __name__ == "__main__":
    main()