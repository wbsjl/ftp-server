from multiprocessing import Pool
from time import sleep,ctime

def worker(msg):

    print(msg)
    sleep(2)
    return 1


pool = Pool(3)

for i in range(20):
    msg = 'HEllO %d'%i
    r=pool.apply_async(func=worker,args=(msg,))
    print(r.get())
pool.close()
pool.join()
