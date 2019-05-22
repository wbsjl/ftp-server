from socket import*

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
s.bind(('0.0.0.0',8888))
s.listen(3)
c,addr= s.accept()

print("地址类型：", s.family)
print("套接子类型",s.type)
print('绑定地址',s.getsockname())
print('描述符：', s.fileno())
print('客户端地址：', c.getpeername())