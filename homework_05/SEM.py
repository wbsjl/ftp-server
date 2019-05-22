from multiprocessing import Semaphore,Process
from time import sleep
import os

sem = Semaphore(3)

def handle():
    print('%d 想执行事件'%os.getpid())
    sem.acquire()
    print('%d 开始执行操作'%os.getpid())
    sleep(3)
    print('%d 完成操作'%os.getpid())
    sem.release()

jobs=[]
for i in range(5):
    p = Process(target=handle)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value())