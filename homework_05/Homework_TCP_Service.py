import socket




sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
sockfd.bind(('0.0.0.0',8888))
# 设置监听
sockfd.listen(100)

# try:

        # 等待处理客户端连接

print("waiting")

connfd,addr = sockfd.accept()
print("Connected by:",addr)
# 收发消息
data = connfd.recv(999999999)
print("hi")
new_one = open('the3.jpg', 'wb')
new_one.write(data)

if not data:
    print('exit')
print("received", data)
n = connfd.send(b'Receive your message')
print("sent %d bytes"%n)


# 关闭套接字
connfd.close()

# except KeyboardInterrupt as a:
#     print('biubiubiu')

sockfd.close()
