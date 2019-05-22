from socket import*
import os,sys
import signal



HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)
#处理僵尸
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("listening the port 8888...")

def handle(c):
    print('客户端:',c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"biu")

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('退出')
    except Exception as e:
        print(e)
        continue


    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c)
        os._exit(0)
    else:
        c.close()

