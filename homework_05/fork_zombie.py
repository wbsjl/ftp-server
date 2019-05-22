import os

pid = os.fork()

if pid < 0:
    pass
elif pid == 0:
    print("child: ", os.getpid())
else:
    while True:
        pass
