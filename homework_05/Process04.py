from multiprocessing import *
from time import sleep,ctime

def tm():
    for i in range(3):
        sleep(2)
        print(ctime())

p =Process(target = tm,name='cxk')
p.daemon = True
p.start()
print('Name: ', p.name)
print('Pid:',p.pid)
print('Alive:', p.is_alive())