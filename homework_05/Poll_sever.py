from socket import  *
from select import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

p =poll()

fdmap={s.fileno():s}

p.register(s,POLLIN|POLLERR)

while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('connected',addr)
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()]=c
        elif event & POLLHUP:
            print('quit')
            p. unregister(fd)
            del fdmap[fd]
        elif event & POLLIN:
            data =fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data.decode())
            fdmap[fd].send(b'OK')