# class StudentModel:
#     """
#         学生数据模型类
#     """
#
#     def __init__(self, name="", age=0, score=0, id=0):
#         """
#             创建学生对象
#         :param id: 编号
#         :param name: 姓名
#         :param age: 年龄
#         :param score: 成绩
#         """
#         self.id = id
#         self.name = name
#         self.age = age
#         self.score = score
#
#     @property
#     def id(self):
#         return self.__id
#
#     @id.setter
#     def id(self, value):
#         self.__id = value
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         self.__age = value
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, value):
#         self.__score = value
#
#
#     def __str__(self):
#         return "名字：%s,年龄%d,成绩%d,ID %d"%(self.name,self.age,self.score,self.id)
#
#     def __repr__(self):
#         return "StudentModel('%s',%d,%d,%d)" % (self.name, self.age, self.score, self.id)
#
#
#
# s01=StudentModel("niconiconi",10,90,100)
# print(s01)
# s02=eval(s01.__repr__())
# print(s02)
# s01.name="咚，哒哟"
# print(s01)
# w=eval("1+1.3")
# print(w)

# class Vector:
#     def __init__(self,x):
#         self.x=x
#
#
#     # def __sub__(self, other):
#     #     return Vector(self.x-other)
#
#
#     # def __rsub__(self, other):
#     #     return Vector(self.x)-Vector(self.x)
#
#     def __iadd__(self,other):
#         self.x+=other
#         return self
#
#     def __str__(self):
#         return "是：%d"%self.x
#
# v01=Vector(10)
# # v02=v01-5
# # print(v02)
# # v02=Vector(2)
# #
# # v03=v02-v01
# # print(v03)
#
# v01 +=2
#
# print(v01)





#
# class EmployerManager:
#     def __init__(self):
#         self.__employers=[]
#
#
#     def add_employers(self,e):
#         if not isinstance(e,Employers):
#             return
#         self.__employers.append(e)
#
#     def calculate_total_salaries(self):
#         total_salaries=0
#         for emp in self.__employers:
#             total_salaries+=emp.salaries()
#         return total_salaries
#


class Employers:
    def __init__(self,name,job):
        self.name=name
        self.job=job
    def total_salaries(self):
        return self.job.salaries()


class Job:
    def __init__(self,basic):
        self.basic=basic

    def salaries(self):
        return self.basic






class Normal(Job):

    def __init__(self,basic):
        super().__init__(basic)


    def salaries(self):
        return self.basic

class Programmer(Job):

    def __init__(self,basic,dividents):
        super().__init__(basic)
        self.dividents=dividents

    def salaries(self):
        return self.basic+ self.dividents

class Sales(Job):
    def __init__(self,basic,amount):
        super().__init__(basic)
        self.amount=amount

    def salaries(self):
        return self.basic+self.amount


zs=Employers("i",Normal(1000))
print(zs.total_salaries())
zs.job=Sales(3000,1000)
print(zs.total_salaries())



# n01=Normal(3000)
# p01=Programmer(7000,4000)
# s01=Sales(5000,3000)
# M01=EmployerManager()
# M01.add_employers(n01)
# M01.add_employers(s01)
# M01.add_employers(p01)
# print(M01.calculate_total_salaries())
