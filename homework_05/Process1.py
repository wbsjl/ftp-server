import multiprocessing as mp
from time import sleep
a=1
def fun01():

    print('子进程开始执行')
    global  a
    print('a= ', a)
    a=10000
    sleep(3)
    print('子进程执行完毕')

def fun02():

    print('miao')

p = mp.Process(target = fun01)
c= mp.Process(target= fun02)

print(a)
p.start()
c.start()
print('hi')

p.join(5)




