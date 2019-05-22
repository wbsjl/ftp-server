from multiprocessing import Queue
from time import sleep
q = Queue(3)


print('empty',q.empty())
q.put(1)

q.put(2)
q.put(3,True,3)
sleep(0.1)
print('empty',q.empty())
print('size',q.qsize())
print('full',q.full())
q.get()
print('size',q.qsize())
q.put(4,True,4)