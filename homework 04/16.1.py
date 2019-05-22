# class Weapon:
#     def __init__(self,atk=0):
#         self.atk=atk
#         self.owned = []
#
#     def purchase(self,w):
#         self.owned.append(w)
#
#
#     def use(self,w):
#
#             if isinstance(w,Weapon):
#                 print("yes")
#                 w.attack()
#                 w.damage_dealed()
#             else:
#                 print("no")
#
#     def attack(self):
#         raise NotImplementedError()
# class Gun(Weapon):
#     def __init__(self,atk_speed,atk):
#         super().__init__(atk)
#         self.atk_speed=atk_speed
#
#     def attack(self):
#         print("shoot")
#     def damage_dealed(self):
#         print(self.atk*self.atk_speed)
#         return self.atk*self.atk_speed
#
#
# class Grenade(Weapon):
#     def __init__(self,atk,range=100):
#         self.range=range
#         super().__init__(atk)
#
#
#     def attack(self):
#         print("explode")
#
#
#     def damage_dealed(self):
#         print(self.atk)
#         return self.atk
#
#
# class Enemy:
#     def __init__(self,range,hp=1000):
#         self.range=range
#         self.hp=hp
#
#     def hurted(self,e):
#         if self.range<=e.range:
#             self.hp-=e.atk
#
#
#
# g01=Gun(0.5,50)
# gr01=Grenade(100,300)
# w01=Weapon()
# w01.purchase(g01)
# w01.purchase(gr01)
# w01.use(gr01)
# e01=Enemy(20,400)
# e01.hurted(gr01)
# print("hp %d"%(e01.hp))









class EmployerManager:
    def __init__(self):
        self.__employers=[]


    def add_employers(self,e):
        if not isinstance(e,Employers):
            return
        self.__employers.append(e)

    def calculate_total_salaries(self):
        total_salaries=0
        for emp in self.__employers:
            total_salaries+=emp.salaries()
        return total_salaries



class Employers:
    def __init__(self,basic):
        self.basic=basic

    def salaries(self):
        pass

class Normal(Employers):

    def __init__(self,basic):
        super().__init__(basic)


    def salaries(self):
        return self.basic

class Programmer(Employers):

    def __init__(self,basic,dividents):
        super().__init__(basic)
        self.dividents=dividents

    def salaries(self):
        return self.basic+ self.dividents

class Sales(Employers):
    def __init__(self,basic,amount):
        super().__init__(basic)
        self.amount=amount

    def salaries(self):
        return self.basic+self.amount


n01=Normal(3000)
p01=Programmer(7000,4000)
s01=Sales(5000,3000)
M01=EmployerManager()
M01.add_employers(n01)
M01.add_employers(s01)
M01.add_employers(p01)
print(M01.calculate_total_salaries())





