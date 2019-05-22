"""
ｇｅｖｅｎｔ协程演示
"""

import gevent
from gevent import monkey
monkey.patch_all()
from socket import *

def handle(c):
    while True:
        try:
            data = c.recv(1024)
            if not data:
                break
        except ConnectionResetError as a:
            print('quit')
            continue

        print(data.decode())
        c.send(b'ok')
    c.close()

s = socket()


s.bind(('0.0.0.0',8888))
s.listen(4)
while True:
    try:
     c,addr = s.accept()
     print("from:", addr)
     # handle(c)
     gevent.spawn(handle, c)
    except ConnectionResetError as e:
        print(quit)
        continue


s.close()