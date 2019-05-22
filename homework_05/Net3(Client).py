from socket import  *

sockfd = socket()

server_addr = ('176.122.17.93',8000)
sockfd.connect((server_addr))


sockfd.send(b'hi')

try:
    while True:

        message=input("enter")
        if not message:
            break
        sockfd.send(message.encode())
        data = sockfd.recv(1024)
        print("from server",data)
except ConnectionResetError as a:
    print('exit')


sockfd.close()