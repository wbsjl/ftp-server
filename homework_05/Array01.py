from multiprocessing import Process,Array

shm = Array('c',b'hello')

def fun():
    for i in shm:
        print(i)
    shm[1]= 4


p = Process(target = fun)
p.start()
p.join()


for i in shm:
    print(i,end=' ')

print(shm.value)