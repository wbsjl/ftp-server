from socket import  *
from select import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

ep =epoll()

fdmap={s.fileno():s}

ep.register(s,EPOLLIN|EPOLLERR)

while True:
    events = ep.poll()
    for fd,event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('connected',addr)
            ep.register(c,EPOLLIN|EPOLLHUP)
            fdmap[c.fileno()]=c
        elif event & EPOLLHUP:
            print('quit')
            ep. unregister(fd)
            del fdmap[fd]
        elif event & EPOLLIN:
            data =fdmap[fd].recv(1024)
            if not data:
                ep.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data.decode())
            fdmap[fd].send(b'OK')