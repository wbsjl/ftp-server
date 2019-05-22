from multiprocessing import Process, Value
import time
import random

money = Value('i',5000)

def man():
    for i in range(30):
        time.sleep(0.05)
        money.value +=random.randint(1,1000)

def girl():
    for i in range(30):
        time.sleep(0.01)
        money.value -=random.randint(100,800)

m = Process(target = man)
g = Process(target = girl)
m.start()
g.start()
m.join()
g.join()

print('余额：', money.value)
