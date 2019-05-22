from time import ctime,time
from multiprocessing import Process
from threading import Thread,activeCount



def count(x,y):
    c = 0
    while c < 7000000:
        c +=1
        x +=1
        y +=1
    print(ctime())

def io():
    write()
    read()
    print(ctime())

def write():
    f = open('test','w')
    for i in range(1500000):
        f.write('hello world\n')
    f.close()

def read():
    f = open('test')
    lines = f.readlines()
    f.close()





# for i in range(10):
#     io()

# for i in range(10):
#     count(1,1)
job=[]

print(ctime())
for i in range(10):
    p = Process(target=count,args=(1,1))
    p.start()




for n in job:

    n.join()



#io单线程10秒,计算单线程10秒
#多进程io4秒,计算6秒
#多线程io8秒,计算１1秒