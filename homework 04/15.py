# class Person:
#
#     def __init__(self,name,money):
#         self.name=name
#         self.money=money
#
#
# class Bank:
#
#
#     def __init__(self,name,money):
#         self.name=name
#         self.money=money
#
#
#     def withdraw(self,person,value):
#         self.money-=value
#         person.money+=value
#         print(self.money)
#         print("取钱")
#
#
#
# xm=Person("小明",0)
# zsxh=Bank("招商银行",10000)
# zsxh.withdraw(xm,1002)




class Object:
    def __init__(self,ad=0,hp=0):
        self.ad=ad
        self.hp=hp


    @property
    def ad(self):
         return self.__ad

    @ad.setter
    def ad(self,value):
        self.__ad=value

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        self.__hp=value

    def attack(self,enemy):
        enemy.hp-=self.ad



e1=Object(10,100)
p1=Object(50,100)


while True:
    p1.attack(e1)
    print("攻击")

    if e1.hp<=0:
        print("死亡")
        e1.hp+=100
        print("复活")
        continue
    e1.attack(p1)
    print("攻击")

    if p1.hp==0:
        print("碎屏")
        break















