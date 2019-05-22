# class Wife:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# class Student:
#     '''
#     　　学生
#     '''
#
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def study(self):
#         print(self.name+"学习")
#
#     def work(self):
#         print(str(self.age)+"工作")
#
# wu_kong=Student("悟空同学",28,"男")
# ba_jie=Student("八戒同学",29,"男")
#
# wu_kong.work()
# ba_jie.study()
#


# class Enemy:
#     """
#     enemy
#     """
#     def __init__(self,name="",hp=0,atk=1,atk_speed=2):
#         self.name=name
#         self.hp=hp
#         self.atk=atk
#         self.atk_speed=atk_speed
#
#     def print_self(self):
#         print(self.name,self.hp,self.atk,self.atk_speed)
#
# list01=[]
#
# for i in range(3):
#     e=Enemy()
#     e.name=str(input("输入名字：　"))
#     e.hp=str(input("输入ｈｐ："))
#     e.atk=str(input("输入攻击力："))
#     e.atk_speed=str(input("输入攻击速度："))
#     list01.append(e)
#
# for item in list01:
#     item.print_self()
#
#
# def search(list01,name):
#     getname=str(input("请输入名字查找：　"))
#     for item in list01:
#         if item.name==name:
#             return item
#
# list02=[
#     Enemy("12",133,21,123),
#     Enemy("11",133,21,123),
#     Enemy("10",133,21,123),
#     Enemy("9",133,21,123),
# ]
#
# re=search(list02,"9")
# re.print_self()


# class Electronic_devices:
#     def __init__(self,type,brand):
#         self.type=type
#         self.brand=brand
#
#     def display(self):
#         print("显示")
#
#
# ed1=Electronic_devices("monitor","hp")
# ed1.display()


# class Furniture:
#     def __init__(self,type,brand):
#         self.type = type
#         self.brand=brand
#
#     def use(self):
#         print("摆放")
#
# fur1=Furniture("chair","unknow")
# fur1.use()
#


class Student:
    def __init__(self,name='',sex='',age=0,grade=0):
        self.name=name
        self.age=age
        self.grade=grade
        self.sex=sex

    def print_self(self):
     print(self.name,self.sex,self.age,self.grade)


list01=[]
for i in range(3):
    e=Student()
    e.name=str(input("输入名字：　"))
    e.age=str(input("输入性别："))
    e.grade=str(input("输入成绩："))
    e.sex=str(input("请输入性别：　"))

    list01.append(e)

getname=str(input("请输入名字查找：　"))


getsex=str(input("请输入性别查找：　"))

def search_by_name(list01, name):

    for item in list01:
        if item.name==name:
            return item

def search_by_sex(list01, sex):
    sexlist=[]
    for item in list01:
        if item.sex==sex:
            sexlist.append(item)
    return sexlist


# re=search_by_name(list01,getname)
resex=search_by_sex(list01,getsex)
# re.print_self()
for e in resex:
    e.print_self()