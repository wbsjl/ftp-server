from socket import *
s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind(('0.0.0.0',9999))

while True:
    try:
        msg,addr = s.recvfrom(1024)
    except KeyboardInterrupt:
        print('exit')
        break
    else:
        print(msg.decode())

s.close()