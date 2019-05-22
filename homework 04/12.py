# class Wife:
#
#     count=0
#     @classmethod
#     def get_count(cls):
#         return Wife.count
#
#
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         Wife.count+=1
#
#
# wf1=Wife("1",18,"女")
# wf2=Wife('2',15,"女")
#
# print(Wife.get_count())


#hp(0-100)
#atek_speed(0-10）

# class Enemy:
#     def __init__(self,name='',atk=0,atk_speed=0,hp=0):
#         self.set_name(name)
#         self.set_atk(atk)
#         self.set_atk_speed(atk_speed)
#         self.set_hp(hp)
#
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self,value):
#         self.__name=value
#
#     def get_atk(self):
#         return self.__atk
#
#     def set_atk(self,value):
#         self.__atk= value
#
#     def get_atk_speed(self):
#         return self.__atk_speed
#
#     def set_atk_speed(self, value):
#         if 0 <= value <= 10:
#             self.__atk_speed = value
#         else:
#             self.__atk_speed = 0
#             print("太高了")
#
#     def get_hp(self):
#         return self.__hp
#
#     def set_hp(self, value):
#         if 0 <= value <= 100:
#             self.__hp = value
#         else:
#             self.__hp = 0
#             print("太多了")
#
# e01=Enemy("cnm",1,100,-1)
#
# print(e01.get_name(),e01.get_hp(),e01.get_atk_speed())

#
# class Enemy:
#     def __init__(self,name='',atk=0,atk_speed=0,hp=0):
#         self.name = name
#         self.atk = atk
#         self.atk_speed = atk_speed
#         self.hp = hp
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
#     @property
#     def atk(self):
#         return self.__atk
#     @atk.setter
#     def atk(self,value):
#         self.__atk= value
#     @property
#     def atk_speed(self):
#         return self.__atk_speed
#     @atk_speed.setter
#     def atk_speed(self, value):
#         if 0 <= value <= 10:
#             self.__atk_speed = value
#         else:
#             self.__atk_speed = 0
#             print("太高了")
#     @property
#     def hp(self):
#         return self.__hp
#     @hp.setter
#     def hp(self, value):
#         if 0 <= value <= 100:
#             self.__hp = value
#         else:
#             self.__hp = 0
#             print("太多了")
#
# e01=Enemy("p",1,100,-1)
#
# print(e01.hp)


# class Zsls:
#     def __init__(self,name,wage):
#         self.name=name
#         self.wage=wage
#         self.skill=[]
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name = value
#
#     @property
#     def wage(self):
#         return self.__wage
#
#     @wage.setter
#     def wage(self,value):
#         self.__wage = value
#
#
#     def teach(self,person_other,str_skill):
#       person_other.skill.append(str_skill)
#       print(self.name,"教了",person_other.name,str_skill)
#
#
#
#     def work(self):
#         print("工作")
#
#
#     def earned(self):
#         print("挣了")
#
# zs=Zsls("张三",8000)
# ls=Zsls("李四",3000)
# zs.teach(ls,"python")
# ls.teach(zs,"游戏")



# nums=[2,7,11,15]
# target=9
# location=[]
# def fine(nums,target,location):
#     for m in range(len(nums)):
#         for n in range(len(nums)):
#             if nums[m]+nums[n]==target:
#                 location.append(nums[m])
#                 location.append(nums[n])
#
#                 break
#         return location
#
# print(fine(nums,target,location))


class Skill:


    __slots__ = ("__name","__cd","__ld","__range")


    def __init__(self,name="",cd=0,ld=0,range=0):
        self.name=name
        self.cd=cd
        self.ld=ld
        self.range=range

    def print_self(self):
        print(self.name,self.cd,self.ld,self.range)



    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value

    @property
    def cd(self):
        return self.__cd
    @cd.setter
    def cd(self,value):
        self.__cd=value

    @property
    def ld(self):
        return self.__ld

    @ld.setter
    def ld(self,value):
        self.__ld=value

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self,value):
        self.__range=value

list01=[]
for i in range(3):
    s=Skill()
    s.name=str(input("输入名字：　"))
    s.cd=int(input("输入cd："))
    s.ld=int(input("输入持续时间："))
    s.range=int(input("输入技能范围："))
    list01.append(s)

# getname=str(input("请输入名字查找：　"))
#
# def search_name(list01, getname):
#
#     for item in list01:
#         if item.name==getname:
#             item.print_self()
#             return item
#
# search_name(list01,getname)
#
# for i in list01:
#     if i.ld>10:
#         i.print_self()


list02=[]
for n in range(len(list01)-1):
    if list01[n].range>list01[n+1].range:
        list02.append(list01[n])

list02[len(list02)-1].print_self()

#
# for m in range(len(list01)-1):
#     if list01[m].ld>list01[m+1].ld:
#         list01[m],list01[m+1]=list01[m+1],list01[m]
#
# for ski in list01:
#     ski.print_self()




