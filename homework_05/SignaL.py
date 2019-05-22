import os
import signal

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()

if pid <0:
    print("failed")
elif pid == 0:
    print('child process:',os.getpid())
    os._exit(2)
else:

    while True:
        pass