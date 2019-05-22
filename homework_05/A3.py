from multiprocessing import Process,Array
from Array01 import *

def change():

    shm[4] =12
    for i in shm:
        print(i)


p = Process(target=change)
p.start()
p.join()
