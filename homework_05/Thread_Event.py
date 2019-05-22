from threading import Event,Thread
from time import sleep

e = Event()
s = None

def yangzirong():
    print("杨子荣前来拜山头")
    global s
    s = '天王盖地虎'
    e.set()

t = Thread(target=yangzirong)

t.start()
e.wait()
print('说对口令就是自己人')
if s =='天王盖地虎':
    print('宝塔镇河妖')
else:
    print('五月加急名单')
t.join()



