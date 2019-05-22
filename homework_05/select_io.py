from socket import *
from select import select


s = socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

print('uploading')
fd = open('log.txt','a')
rs, ws, xs = select([s],[fd],[])

print('rs',rs)
print('ws',ws)
print('xs',xs)