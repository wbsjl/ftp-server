from socket import  *
sockfd = socket()
i=open('123.jpg','rb',-1)
# i.seek(0)


server_addr = ('176.122.17.93',8888)
sockfd.connect((server_addr))
try:
        sockfd.send(i.read())
        data = sockfd.recv(999999999)
        print("from server",data)
except ConnectionResetError as a:
    print('exit')


sockfd.close()