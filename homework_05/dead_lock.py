import time
import threading


class Account:

    def __init__(self, _id,balance,lock):
        self.id = _id
        self.balance = balance
        self.lock = lock

    def withdraw(self,amount):
        self.balance -=amount

    def deposit(self,amount):
        self.balance +=amount

    def check(self):
        return self.balance

def transfer(from_,to,amount):
    if from_.lock.acquire():
        from_.withdraw(amount)
        time.sleep(0.5)
        if to.lock.acquire():
            to.deposit(amount)
            to.lock.release()
        from_.lock.release()
    print('finished')



you = Account('you',5000,threading.Lock())
kunkun = Account('蔡徐坤',3000,threading.Lock())

t=threading.Thread(target=transfer,args=(you,kunkun,500))
p=threading.Thread(target=transfer,args=(kunkun,you,500))
t.start()
time.sleep(3)
p.start()
t.join()
p.join()
print("you: ",you.check())
print("kunkun",kunkun.check())