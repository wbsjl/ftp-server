from threading import Thread

class ThreadClass(Thread):
    def __init__(self,attr):
        self.attr =attr
        super().__init__()


    def fun01(self):
        print('1')

    def fun02(self):
        print('2')

    def run(self):
        self.fun01()
        self.fun02()

t = ThreadClass(4)
t.start()
t.join()