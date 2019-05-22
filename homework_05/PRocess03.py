from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print('I am %s'%name)
        print('i am working.....')


# p = Process(target = worker,args=(2,'Baron'))
# p = Process(target = worker,kwargs={'name':"miao",'sec':2})
p = Process(target = worker,args=(2,),kwargs={'name':"miao"})
p.start()
p.join()
