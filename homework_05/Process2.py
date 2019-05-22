import multiprocessing as mp
from time import sleep
import os
a=1
def fun01():
    sleep(2)
    print('nico',os.getpid(),os.getppid())

def fun02():
    sleep(3)
    print('nic',os.getpid(),os.getppid())

def fun03():
    sleep(4)
    print('oni',os.getpid(),os.getppid())

things = [fun01,fun02,fun03]
jobs=[]
for i in things:
    p = mp.Process(target = i)
    jobs.append(p)
    p.start()

for j in jobs:
    j.join()

