from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print('线程属性测试')

t = Thread(target=fun,name='02')
t.start()

p =Thread(target=fun,name='016')
p.setDaemon(True)
p.start()

t.setName('nico')
print(p.getName())
print(t.getName())
t.join()
print(p.isAlive())
