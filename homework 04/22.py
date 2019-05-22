#
# list01=["悟空","八戒","沙僧","唐僧"]
# iterator=list01.__iter__()
#
# while True:
#     try:
#         item=iterator.__next__()
#         print(item)
#
#     except StopIteration:
#         break


# dict01={"张三丰":101,"张无忌":102,"赵敏":102}
#
# iterator2 = dict01.__iter__()
# value=iter(dict01.values())
#
# while True:
#     try:
#         item = iterator2.__next__()
#         print(item,dict01[item])
#
#     except StopIteration:
#         break

#
# for k,v in dict01.items():
#     print(k,v)

#
#
# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
#
#
# class EmployeeManager:
#     def __init__(self,employees):
#         self.employee=employees
#
#     def __iter__(self):
#         # return EmployeeIterator(self.employee)
#         for item in self.employee:
#             yield item
#
#
#
#
# # class EmployeeIterator:
# #     def __init__(self,target):
# #         self.target=target
# #         self.count=0
# #
# #     def __next__(self):
# #         if self.count>len(self.target)-1:
# #             raise StopIteration
# #
# #         item=self.target[self.count]
# #         self.count+=1
# #         return item
#
# manager=EmployeeManager([Employee("1","2"),Employee("3","3")])
#
#
#
# iterator=manager.__iter__()
#
# while True:
#     try:
#         item=iterator.__next__()
#         print(item)
#
#     except StopIteration as e:
#         print(e)
#         break
#
#
# # for item in manager:
# #     print(item)






#
# class MyrangeI:
#     def __init__(self,therange):
#         self.therange=therange
#         self.count=0
#
#
#     def __next__(self):
#         if self.count>self.therange-1:
#             raise StopIteration
#         item =self.count
#         self.count+=1
#
#         return item

# class Myrange:
#     def __init__(self,num):
#         self.num=num
#
#     def __iter__(self):
#         # return MyrangeI(self.num)
#         ## for i in range(self.num):
#         ##     yield i
#         start=0
#         while start<self.num:
#             yield start
#             start+=1
#
#
# it=Myrange(5).__iter__()
#
# while True:
#     try:
#         item=it.__next__()
#         print(item)
#     except StopIteration:
#         break


#
# for item in Myrange(2):
#     print(item)



# list01=[1,2,3,4,5,6,7,8,9,0]
#
# class Pick:
#     def __init__(self,the_range):
#         self.the_range=the_range
#
#
#     def __iter__(self):
#         for item in self.the_range:
#                 if item%2==0:
#                     yield item
#
#
# it=Pick(list01).__iter__()
#
# while True:
#     try:
#         item=it.__next__()
#         print(item)
#     except StopIteration:
#         break


# class Student:
#     def __init__(self,name,sex,age,score):
#         self.name=name
#         self.sex=sex
#         self.age=age
#         self.score=score
#     def __str__(self):
#         return "%s,%s,%d,%d"%(self.name,self.sex,self.age,self.score)
#
#
# list_stu=[Student("张无忌","男",28,82),
#           Student("赵敏","女",25,95),
#           Student("周芷若","女",26,88)]
#
# class Choose:
#     def __init__(self,length):
#         self.length=length
#
#     def __iter__(self):
#         for item in range(len(self.length)):
#             if self.length[item].sex =="女":
#                 yield self.length[item]
#
# it=Choose(list_stu).__iter__()
#
# while True:
#     try:
#         item=it.__next__()
#         print(item)
#     except StopIteration:
#         break




# class Student:
#     def __init__(self,name,sex,age,score):
#         self.name=name
#         self.sex=sex
#         self.age=age
#         self.score=score
#     def __str__(self):
#         return "%s,%s,%d,%d"%(self.name,self.sex,self.age,self.score)
#
#
# list_stu=[Student("张无忌","男",28,82),
#           Student("赵敏","女",25,95),
#           Student("周芷若","女",26,88)]
#
# class Choose:
#     def __init__(self,length):
#         self.length=length
#
#     def __iter__(self):
#         for item in range(len(self.length)):
#             if self.length[item].score >90:
#                 yield self.length[item]
#
# it=Choose(list_stu).__iter__()
#
# while True:
#     try:
#         item=it.__next__()
#         print(item)
#     except StopIteration:
#         break

# class Skill:
#     def __init__(self,code,name,cd,ad,mc):
#         self.code=code
#         self.name=name
#         self.cd=cd
#         self.ad=ad
#         self.mc=mc
#     def __str__(self):
#         return ("%d,%s,%d,%d,%d"%(self.code,self.name,self.cd,self.ad,self.mc))
#
# class search:
#     def __init__(self,length):
#         self.length=length
#     def __iter__(self):
#         for item in self.length:
#             if item.ad>10 and item.mc==0:
#              yield item
#
# skills=search([Skill(101,'a',10,14,5),Skill(102,'b',19,20,7),Skill(103,'c',0,5,1),Skill(104,'d',4,20,0)])
# iterator=skills.__iter__()
#
# while True:
#     try:
#         item=iterator.__next__()
#         print(item)
#     except StopIteration:
#         break




# class Skill:
#     def __init__(self,code,name,cd,ad,mc):
#         self.code=code
#         self.name=name
#         self.cd=cd
#         self.ad=ad
#         self.mc=mc
#     def __str__(self):
#         return ("%d,%s,%d,%d,%d"%(self.code,self.name,self.cd,self.ad,self.mc))
#
# def search(length):
#         for item in length:
#             if item.ad>10 and item.mc==0:
#              yield item
#
#
#
# skills=search([Skill(101,'a',10,14,5),Skill(102,'b',19,20,7),Skill(103,'c',0,5,1),Skill(104,'d',4,20,0)])
# iterator=skills.__iter__()
#
# while True:
#     try:
#         item=iterator.__next__()
#         print(item)
#     except StopIteration:
#         break














