

# list01=['a','b','c','d','e','f']

# def my_enumerate(the_list):
#     for item in range(len(the_list)):
#         yield((str(item),str(the_list[item])))
#
# my_enumerate(list01)

# list02=[1,2,3,4]
#
# def my_zip(list1,list2):
#
#     if len(list1)>len(list2):
#         for item in range(len(list2)):
#             yield((list1[item],list2[item]))
#     else:
#             for item in range(len(list1)):
#                 yield((list1[item], list2[item]))
#
#
# iterator=my_zip(list02,list01).__iter__()
#
# while True:
#     try:
#         item=iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
#
#
#
# my_zip(list01,list02)



# list03=[2,3,4,6]
# result=[item for item in list03 if item>3]
#
# for item in result:
#     print(item)
#
#
#
#
# result=(item for item in list03 if item>3)
# for item in result:
#     print(item)


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
# list01=[
#     Skill(101, 'a', 10, 14, 5),
#      Skill(102, 'b', 19, 20, 7),
#      Skill(103, 'c', 0, 5, 1),
#      Skill(104, 'd', 4, 20, 0)
# ]
#
#
# result1=[item for item in list01 if (item.mc==0 and item.ad>10)]
# for i in result1:
#     print(i)
#
#
# result2=(item for item in list01 if (item.mc==0 and item.ad>10))
# for i in result2:
#     print(i)

from my_tools import list_selecter




#
# class Skill:
#     """
#
#     """
#     def __init__(self,code,name,cd,ad,mc):
#         self.code=code
#         self.name=name
#         self.cd=cd
#         self.ad=ad
#         self.mc=mc
#     def __str__(self):
#         return ("%d,%s,%d,%d,%d"%(self.code,self.name,self.cd,self.ad,self.mc))
#
# def find_all(list,condition):
#         """)
#         :param list:
#         :param condition:
#         :return:
#         """
#         for item in list:
#             if condition(item):
#              yield item
#
#
# def cond_cd(item):
#     return item.cd==0
#
#
# def cond_ad(item):
#     return item.ad >5
#
#
# def cond_admc(item):
#     return item.ad> 10 and item.mc==0
#
#
# list01=[
#     Skill(101, 'a', 10, 14, 5),
#      Skill(102, 'b', 19, 20, 7),
#      Skill(103, 'c', 0, 5, 1),
#      Skill(104, 'd', 4, 20, 0)
# ]


# for item in list_selecter.find_all(list01,lambda item:item.ad>5):
#     print(item)
#
#
#
# for item in find_all(list01,lambda item:item.cd==0):
#     print(item)
#
# for item in find_all(list01,lambda item:item.ad>10 and item.mc==0):
#     print(item)

# iterator=find_all(list01.__iter__(),cond_cd)
#
# while True:
#     try:
#         item=iterator.__next__()
#         print(item)
#     except StopIteration:
#         break





# class Skill:
#     """
#
#     """
#     def __init__(self,code,name,cd,ad,mc):
#         self.code=code
#         self.name=name
#         self.cd=cd
#         self.ad=ad
#         self.mc=mc
#     def __str__(self):
#         return ("%d,%s,%d,%d,%d"%(self.code,self.name,self.cd,self.ad,self.mc))
#
# def find_all(list,condition):
#         """)
#         :param list:
#         :param condition:
#         :return:
#         """
#         for item in list:
#             if condition(item):
#              yield item
#
#
# def cond_cd(item):
#     return item.cd==0
#
#
# def cond_ad(item):
#     return item.ad >5
#
#
# def cond_admc(item):
#     return item.ad> 10 and item.mc==0
#
#
# list01=[
#     Skill(101, 'a', 10, 14, 5),
#      Skill(102, '降龙十八掌', 19, 20, 7),
#      Skill(101, 'c', 0, 5, 1),
#      Skill(104, '降龙十八掌', 4, 20, 0)
# ]
#
#
# for item in list_selecter.list_select.find_all(list01,lambda item:item.code==101):
#     print(item)
#
#
# for item in list_selecter.list_select.find_all(list01,lambda item:item.name=='降龙十八掌'):
#     print(item)
#     break
#
# for item in list_selecter.list_select.find_all(list01,lambda item:item.cd>10):
#     print(item)
#     break

# from my_tools import list_selecter
#
# class Skill:
#     """
#
#     """
#
#     def __init__(self, code, name, cd, ad, mc):
#         self.code = code
#         self.name = name
#         self.cd = cd
#         self.ad = ad
#         self.mc = mc
#
#     def __str__(self):
#         return ("%d,%s,%d,%d,%d" % (self.code, self.name, self.cd, self.ad, self.mc))
#
#
# def find_all(list, condition):
#     """)
#     :param list:
#     :param condition:
#     :return:
#     """
#     for item in list:
#         if condition(item):
#             yield item
#
#
# def cond_cd(item):
#     return item.cd == 0
#
#
# def cond_ad(item):
#     return item.ad > 5
#
#
# def cond_admc(item):
#     return item.ad > 10 and item.mc == 0
#
#
# list01 = [
#     Skill(101, 'a', 10, 14, 5),
#     Skill(102, '降龙十八掌', 19, 20, 7),
#     Skill(101, 'c', 0, 5, 1),
#     Skill(104, '降龙十八掌', 4, 20, 0)
# ]
#
# list04=list(list_selecter.list_select.select_info(list01,lambda i:i.name))
# print(list04)
#
#
# result=list_selecter.list_select.count(list01,lambda i:i.code)
# print(result)


# def count(list01):
#     sum=0
#     for item in list01:
#         sum+=item.code
#     return sum
#
# print(count(list01))



class Enemy:
    def __init__(self,id,name,atk,hp,asp):
        self.id=id
        self.name=name
        self.atk=atk
        self.hp=hp
        self.asp=asp

list01=[
    Enemy(101,'a',10,0,4),
    Enemy(102,'b',19,160,7),
    Enemy(103,'c',15,0,5),
    Enemy(104,'d',8,90,9),
    Enemy(105,'e',15,2,20),

]

print('----死人------')

for i in list_selecter.list_select.find_all(list01,lambda item: item.hp==0):
    print(i.id)
print('----１０１------')
for i in list_selecter.list_select.find_all(list01,lambda item: item.id==101):
    print(i.id)
print('-----活人--------')
for i in list_selecter.list_select.find_all(list01,lambda item: item.hp>0):
    print(i.id)
print('-----总ａｄ-------')
result= list_selecter.list_select.count(list01,lambda item: item.atk)
print(result)
print('-----攻击速度-------')
for i in list_selecter.list_select.find_all(list01,lambda item: 5<item.asp<10):
    print(i.id)
print('-----名字------')
for i in list_selecter.list_select.find_all(list01,lambda item: item.name):
    print(i.name)
print('-----最后活人-------')
result=list_selecter.list_select.find_last_one(list01,lambda item: item.hp>0)
print(result.name)

print('------最后攻速-----')

result=list_selecter.list_select.find_last_one(list01,lambda item: 5<item.asp)
print(result.name)
print('------总活人-----')
result2=list_selecter.list_select.condiction_count(list01,lambda item: item.hp>0)
print(result2)

print('-------总２０攻速-----')
result3=list_selecter.list_select.condiction_count(list01,lambda item: item.asp<20)
print(result3)
print('--------是否--------')
i=list_selecter.list_select.judge_one(list01,lambda item: item.hp==0)
print(i)
print('--------删除---------')
for i in list_selecter.list_select.delete_all(list01,lambda item: item.atk<5):
    print(i.id)
print('--------最大---------')
x=list_selecter.list_select.find_max(list01,lambda item: item.atk)
print(x)
print('--------升序---------')
m=list_selecter.list_select.sort_list_low_to_high(list01,lambda item: item.atk)
print(m)
print('--------降序---------')
m=list_selecter.list_select.sort_list_high_to_low(list01,lambda item: item.atk)
print(m)
print('--------万能排序---------')
list_selecter.list_select.sort_list(list01,lambda item,c: item.atk<c.atk)
print(list01)


#
# for item in filter(lambda item:item.id>102,list01):#筛选信息
#     print(item.id)
#
# for item in map(lambda item:item.name,list01):#展示信息
#     print(item)
#
# for item in sorted(list01,key=lambda e:e.hp):#升序
#     print(item.hp)
#
# for item in sorted(list01,key=lambda e:e.hp,reverse=True):#降序
#     print(item.hp)
#
# result=max(list01,key=lambda e:e.atk)
# print(result.id)








