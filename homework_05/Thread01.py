import threading
from time import sleep
import os
a=1
def music():
    for i in range(5):
        global a
        a = 100000
        # sleep(2)
        print("播放鸡你太美",os.getpid())

def music2():
    for i in range(5):
        # sleep(2)
        print("播放心如止水",os.getpid())

t =threading.Thread(target=music)
p = threading.Thread(target= music2)
t.start()
p.start()
for i in range(3):
    # sleep(2)
    print("播放niconiconi",os.getpid())
t.join()
p.join()
print(a)

