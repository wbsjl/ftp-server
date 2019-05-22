import os
from time import sleep
pid = os.fork()

if pid<0:
    print("Create process failed")
elif pid ==0:
    sleep(5)
    print("THe new process")
else:
    sleep(4)
    print("the old process")

print("For test over")