from socket import *


def handle(connfd):
    print("request from", connfd.getpeername())
    request = connfd.recv(4096)

    if not request:
        return
    request_line= request.splitlines()[0].decode()
    info = request_line.split(' ')[1]
    if info == '/':
        f = open('index.html')
        response = "HTTP/1.1 200 OK \r\n"
        response += "Conten t-Type: text/html\r\n"
        response += '\r\n'
        response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found \r\n"
        response += "Content-Type: text/html\r\n"
        response += '\r\n'
        response += "<h1>NO</h1>"
    connfd.send(response.encode())



def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(3)
    print("listen ")
    while True:
        connfd,addr=sockfd.accept()
        handle(connfd)
        connfd.close()



if __name__ == "__main__":
    main()