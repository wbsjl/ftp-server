import socket

sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
sockfd.bind(('0.0.0.0',8888))
# 设置监听
sockfd.listen(100)

try:
    while True:
        # 等待处理客户端连接
        print("waiting")

        connfd,addr = sockfd.accept()
        print("Connected by:",addr)
        print(connfd)

        # 收发消息

        while True:
            data = connfd.recv(1024)
            if not data:
                print('exit')
                break
            print("received", data)
            n = connfd.send(b'Receive your message')
            print("sent %d bytes"%n)


        # 关闭套接字
        connfd.close()

except KeyboardInterrupt as a:
    print('biubiubiu')

sockfd.close()

