class Pet:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print("吃")


class Dog(Pet):
    def __init__(self,work,name):
        super().__init__(name)
        self.work = work


    def guard(self):
        print("防守")



# class Bird(Pet):
#
#
#
#     def fly(self):
#         print("飞")
#
# p01=Pet("miao")
# d01=Dog("汪","a")
# b01=Bird()
#
# print(isinstance(d01,Pet))
# print(isinstance(p01,(Bird,Pet)))
# print(issubclass(Pet,Pet))
# print(issubclass(Bird,Dog))

# print(d01.work)






#
# class Ammunition:
#
#     def __init__(self,atk):
#         self.atk=atk
#
#
#     def explode(self,*args):
#         for item in args:
#             if not isinstance(item, Damageable):
#                 print("类型不兼容")
#                 return
#             item.damage(self.atk)
#
#
# class Creatures():
#     def hurt(self):
#         raise NotImplementedError()
#
# class Enemy(Creatures):
#     def hurt(self):
#         print("受伤了")
#
# class Player(Creatures):
#     def hurt(self):
#         print("受伤了")





class ShapeManager:
    def __init__(self):
       self.__graphics=[]



    def add_shape(self,a):
        if not isinstance(a,Surface_area):
            return
        else:
            self.__graphics.append(a)


    def get_total_area(self):

        total_area=0
        for item in self.__graphics:
            total_area+= item.calculate()
        return total_area



class Surface_area():

    def calculate(self):
        pass

class Triangle(Surface_area):

    def __init__(self,bottom,height):
        self.bottom=bottom
        self.height=height



    def calculate(self):

        return self.bottom*self.height/2




class circle(Surface_area):
    def __init__(self,radius):
        self.radius=radius

    def calculate(self):
        return self.radius**2*3.14


t01=Triangle(20,100)
s01=ShapeManager()
s01.add_shape(t01)
print(s01.get_total_area())








