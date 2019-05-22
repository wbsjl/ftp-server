"""
ｉo多路复用ｓｅｌｅｃｔ实现多客户端通信
重点代码
"""

from socket import *
from select import select



s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)


rlist=[s]
wlist=[]
xlist=[]

while True:
    rs, ws, xs = select(rlist, wlist, xlist)

    for r in rs:
        if r is s:
            c, addr = r.accept()
            print('connext from ',addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue

            print(data.decode())
            wlist.append(r)
            r.send(b'yo')

    for w in ws:
        w.send(b'OK,Thanks')
        wlist.remove(w)
    for x in xs:
        pass
