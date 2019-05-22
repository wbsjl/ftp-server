from multiprocessing import Process,Array
from Array01 import shm

def change():
    for i in shm:
        print(i)
    shm[1] =12
   

p = Process(target=change)
p.start()
p.join()

