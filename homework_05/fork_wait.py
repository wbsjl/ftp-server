import os
import time

pid = os.fork()

if pid <0:
    print("failed")
elif pid == 0:
    print('chile process:',os.getpid())
    os._exit(2)
else:
    while True:
        time.sleep(1)
        pid,status= os.waitpid(-1,os.WNOHANG)
        print('pid',pid)
        print('status',status//256)
        while True:
            pass