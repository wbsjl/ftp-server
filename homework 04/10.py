# def fun(a,b,c):
#     a=100
#     b[0]=200
#     c=300
#
# num01=1
# list01=[2]
# list02=[3]
# fun(num01,list01,list02)
#
# print(num01)
# print(list01)
# print(list02)


# set01={1,2,3,4,5,6,7,8}
# set01.clear()
# print(set01)
#

# g01=0
# def plus():
#     global g01
#     g01+=1
# for t in range(5):
#     plus()
#  print(g01)


# 实参的传递方式
# def fun01(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#


#实参传递方式：
# #  位置传参：实参与形参位置对应
# fun01(1,2,3)
#
# #序列传参：用＊将序列拆分后的位置传参，运行是可以根据某些逻辑决定传入数据（列表）
# fun01(*[4,5,6])

#关键字传参：根据名字赋值
# fun01(a=1,c=2,b=3)

#字典传参：用＊＊将字典拆分后变成关键字传参，运行是可以根据某些逻辑决定传入数据（字典）
# fun01(**{'a':1,'c':2,'b':3})


#形参传递方式：
#缺省参数（默认参数）:让调用者可以有选择性的传递需要的信息
# def fun02(a=0,b=1,c=2):
#     print(a)
#     print(b)
#     print(c)
# fun02()
# fun02(1)
# fun02(1,**{'b':'ww'})


# def count_sec(day=0,hour=0,minute=0):
#     int_total_seconds=hour*60*60+day*3600*24+minute*60
#     return int_total_seconds
#
# s01=count_sec(1,1,1)
# print(s01)


#星号元组形参：#双星号字典形参：对于方法内部而言，他就是字典，使用者可以无限制输入位置
# def plus(*args):
#     sum=0
#     for item in args:
#         sum+=item
#     return sum
#
# print(plus(1,2,3,4,5,6))

# #命名关键字形参：强制使用关键字实参：
# def fun1(*,a,b):
#     print(a)
#     print(b)
#
# def fun2(*a,b):
#     print(a)
#     print(b)
#
# fun1(a=2,b=3)
# fun2(1234,123,123,123,b=13)
#
# #双星号字典形参：对于方法内部而言，他就是字典，使用者可以无限制输入关键字
# def fun05(**kwargs):
#     print(kwargs)
#
# fun05(a=1,b=2)


# def fun06(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# fun06(1,2,3,4,5,6,7,a=1,b=2)

# def fun06(a,b,*args,c,d,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(d)
#     print(kwargs)
#
# fun06(1,2,1,2,3,4,c=1,d=2,r=4)

# 1.自定义列表的排序函数
# ２．自学字符串，列表，字典常用函数
# 3. 英文单词反转
# ４，预习面向对象


# def sort(list01):
#     for i in range(len(list01)-1):
#
#         for n in range(i+1,len(list01)):
#             if list01[i]<list01[n]:
#                 list01[i],list01[n]=list01[n],list01[i]
#     print(list01)
#
# sort([1,2,3,4,5,6])

#
#
# def reverseEng(a):
#     splist=a.split(" ")
#     splist.reverse()
#     list01=" ".join(splist)
#     print(list01)
#
# reverseEng("wo L G D shi bu ke zhan sheng de")






