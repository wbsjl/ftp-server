import os
import time

pid = os.fork()

if pid < 0:
    print("error")

elif pid == 0:
    time.sleep(4)
    print('child pid: ', os.getpid())
    print('baba pid: ', os.getppid())
else:

    print(pid)
    print('parent pid:', os.getpid())
    print('grandparent pid:', os.getppid())
