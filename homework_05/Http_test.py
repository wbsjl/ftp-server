from socket import *


s = socket()
s.bind(('0.0.0.0',8100))
s.listen(3)
c,addr= s.accept()
print("connected with",addr)


data=c.recv(4096)

print(data)
data = """HTTP/1.1 200 OK
Content-type:text/html

<h2>hello earth</h2>
"""

c.send(data.encode())

c.close()
s.close()
