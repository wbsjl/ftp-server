import os
from time import *

def f1():
    for i in range(4):
        sleep(2)
        print("写代码。。。")


def f2():
    for i in range(5):
        sleep(1)
        print("测代码。。。")

pid = os.fork()

if pid < 0:
    print('Error')

elif pid == 0:
    print(os.getpid())
    p = os.fork()

    if p == 0:
        sleep(2)
        f2()
        print(os.getppid())
    else:
        os._exit(0)

else:
    os.wait()
    f1()