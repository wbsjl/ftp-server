from multiprocessing import Pipe,Process
import os,time

fd1,fd2 = Pipe(False)

def fun(name):
    time.sleep(3)
    fd2.send({name:os.getpid()})

jobs=[]
for i in range(5):
    p = Process(target= fun,args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()
