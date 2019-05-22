from socket import *
from time import *

f = open('log.txt','w+')
s = socket()
s.bind(('0.0.0.0',8888))
s.listen(4)
s.setblocking(True)
s.settimeout(3)

while True:
    print('waiting ...')
    try:
        c,addr = s.accept()
    except Exception as e:
        sleep(2)
        f.write("%s: %s\n"%(ctime(),e))
        f.flush()


    else:
        data= c.recv(1024).decode()
        print(data)