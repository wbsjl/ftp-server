from threading import Thread
from time import sleep,ctime

class MyThread(Thread):
    def __init__(self,target=None,args=(),kwargs={},name='T'):
        super().__init__()
        self.target=target
        self.args=args
        self.kwargs = kwargs
        self.name=name


    def run(self):
        self.target(*self.args,**self.kwargs)


def player(sec,song):
    for i in range(2):
        print("playing %s:%s"%(song,ctime()))
        sleep(sec)

t = MyThread(target=player, args=(3,),kwargs={'song':'凉凉'},name='happy')
print(t.getName())
t.run()
t.start()
t.join()
