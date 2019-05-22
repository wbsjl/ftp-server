from socket import  *
from time import sleep

class QuitError(Exception):
    pass


class Ftpclient():
    def __init__(self,sockfd):
        self.sockfd = sockfd


    def do_list(self):
        self.sockfd.send(b'L ')

        data = self.sockfd.recv(1024)
        if data == b'  ':
            print(data.decode())
            # while True:
            data2=self.sockfd.recv(1024)
            # if data2 ==b'##':
            print(data2.decode())
        else:
            print(data)

    def do_quit(self):

        self.sockfd.send(b'Q ')
        self.sockfd.close()
        print('quit')
        raise QuitError()
    def do_download(self):
        filename=input('filename:')
        self.sockfd.send(('G '+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'open succesfully':
            fd = open(filename,'wb')
            print('yes')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)
    def do_upload(self):
        filename = input('filename')
        self.sockfd.send(('U '+filename).encode())
        data= self.sockfd.recv(128).decode()
        print(data)
        if data == 'ready':
            try:
                fd = open(filename,'rb')
            except Exception as a:
                print('no ')
                return
            else:
                print('ok')
            while True:
                data = fd.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)

def request(sockfd):
    ftp =Ftpclient(sockfd)
    while True:
        print('\n命令：')
        print('......list......')
        print('......download......')
        print('......upload......')
        print('......quit......')
        cmd = input('your option:')
        if cmd.strip() == 'list':
            ftp.do_list()
        if cmd.strip() == 'download':
            # filename = cmd.strip().split(' ')[-1]
            ftp.do_download()
        if cmd == 'upload':
            ftp.do_upload()
        if cmd.strip() == 'quit':
            try:
                ftp.do_quit()
            except QuitError as a:
                print('已退出')
            break


def main():
    sockfd = socket()
    server_addr = ('176.122.17.93',8888)
    try:
        sockfd.connect((server_addr))
    except Exception as e:
        print('链接失败')
        return
    else:
        print("""
        Data   File   Image
        """)
        cls = input('行输入文件种类:')
        if cls not in['Data','File','Image']:
            print('input error')
            return
        else:
            sockfd.send(cls.encode())
            request(sockfd)
    #
    # try:
    #     while True:
    #
    #         message=input("enter")
    #         if not message:
    #             break
    #         sockfd.send(message.encode())
    #         data = sockfd.recv(1024)
    #         print("from server",data)
    # except ConnectionResetError as a:
    #     print('exit')


    sockfd.close()

if __name__ == "__main__":
    main()
