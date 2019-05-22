from socket import*
from select import*
from multiprocessing import Process

class HTTP_server:
    def __init__(self,server_addr,static_dir):
        self.server_addr = server_addr
        self.static_dir =static_dir
        self.create_socket()
        self.bind()
        self.rlist = [self.s]
        self.wlist = []
        self.xlist = []
    def create_socket(self):
        self.s = socket()
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self):
        self.s.bind(self.server_addr)
        self.ip = self.server_addr[0]
        self.port = self.server_addr[1]

    def serve_forever(self):
        self.s.listen(5)
        print('listen the port %d'%self.port)
        self.rlist.append(self.s)

        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            a = ''
            for r in rs:
                a = r
                if r is self.s:
                    c,addr = self.s.accept()
                    print('connect from',addr)
                    self.rlist.append(c)
                else:
                    self.handle(r)


    def handle(self,connfd):
        request = connfd.recv(4096)

        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print(connfd.getpeername(),':',info)
        #info分为网页和其他
        if info == '/' or info[-5:] == '.html' or info == '/index' or info == '/index.html':
            print(info)
            self.get_html(connfd,info)
            # connfd.close()
        else:
            self.get_data(connfd,info)



    def get_html(self,connfd,info):
        if info =='/' or info == '/index' or info == '/index.html':
            filename = self.static_dir + '/index.html'
            self.open_page(filename,connfd)
        elif info[:6]=='/index' and info[-5:] == '.html':
            print(info[7:])

            filename = self.static_dir + '/'+info[7:]
            self.open_page(filename, connfd)
        else:
            responseHearders = 'HTTP/1.1 200 OK\r\n'
            responseHearders += '\r\n'
            responseBody = '<h1>wait for 3.0</h1>'
            response = responseHearders + responseBody
            connfd.send(response.encode())
    def open_page(self,filename,connfd):
        try:
            fd = open(filename)
        except Exception as a:

            responseHearders = 'HTTP/1.1 404 Not Found\r\n'
            responseHearders += '\r\n'
            responseBody ="<h1>No such page</h1>"
        else:
            responseHearders = 'HTTP/1.1 200 OK\r\n'
            responseHearders += '\r\n'
            responseBody = fd.read()
        finally:
            response =  responseHearders + responseBody
            connfd.send(response.encode())
            connfd.close()






    def get_data(self,connfd,info):
        responseHearders = 'HTTP/1.1 200 OK\r\n'
        responseHearders += '\r\n'
        responseBody = '<h1>wait for 3.0</h1>'
        response = responseHearders +responseBody
        connfd.send(response.encode())

if __name__ == '__main__':
    server_addr = ('0.0.0.0',8000)
    staic_dir = '/home/tarena/Project/static'

    httpd = HTTP_server(server_addr, staic_dir)

    while True:
        t = Process(target=httpd.serve_forever())
        t.start()


