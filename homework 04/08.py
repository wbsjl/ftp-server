# import copy
# list1=[1,[2,3]]
# list2=copy.deepcopy(list1)
# list1[1][0]=233
# print(list2[1][0])



#
# list01=[num for num in range(1,11)]
# list02=[oddnum for oddnum in list01 if oddnum%2!=0]
# list03=[evennum for evennum in list01 if evennum%2==0]
# list04=[larger3 for larger3 in list01 if larger3>3]
#
# print(list04)
#

#
# tup2=(1,'e','b')
# print(tup2)

# th1=(1,3,5,7,8,10,12)
# th0=(4,6,9,11)
# getMonths=int(input("请输入一个月份"))
# if getMonths in th1:
#    print("三十一天")
# elif getMonths in th0:
#    print("三十天")
# elif getMonths==2:
#    print("二十八天")
# else:
#    print("请输入月份１～１２")



# Sum=1
# days=(31,28,31,30,31,30,31,31,30,31,30,31)
# # requestM=int(input("请输入月份：　"))
# # requestD=int(input("请输入日: "))
# # for i in range(requestM-1):
# #     Sum+=days[i]
# # Sum+=requestD
# # print(Sum)


# dictionary={'w':'asdafgafe','q':'qweqwe'}
# print(dictionary['w'])

# getSeason=str(input("输入一个季度　"))
# seasons={
#         '春':'１，２，３',
#          '夏':'４，５，６',
#          '秋':'７，８，９',
#          '冬':'１０，１１，１２'}
# # if getSeason not in seasons:
# #     print("春夏秋冬随便输一个")
# # else:
# #
# #     print(seasons[getSeason])
# del seasons['春']
# print(seasons)

# get=str(input("enter"))
# string={}
# for item in get:
#     if item not in string:
#         string[item]=1
#     else:
#         string[item]+=1
# print(string)

#
# list01=["张三丰","无忌","赵敏"]
# dic01={}
# for names in list01:
#
#        dic01[names]=len(names)
#
# print(dic01)

#
# names=["张三丰","无忌","赵敏"]
# num=[101,102,103]
# dic={}
# x=0
# for item in names:
#     dic[item]=num[x]
#     x+=1
#
# dic2={}
#
# for k,v in dic.items():
#     dic2[v]=k
# dic2={v:k for k,v in dic.items() }
#
# print(dic2)



# list01 = ["a",(1,2,3),{"b":"B","c":"C"}]
# list02 = list01
# list03 = list01[:]
# list02[0] = "b"
# print(list01[0])# ?
# list02[2]["b"] = "BB"
# print(list02[2]["b"])# ?
# list03[0] = "bb"
# print(list01[0])# ?




# 控制台中录入五个学生信息（姓名／年龄／性别）
# 列表中嵌套字典


# 猜拳，系统随机出拳．在系统中岁循环猜测
# 将策略存入容器
# 将用户猜的和系统出的形成一个元组



list01=[]
dic={}
for i in range(5):
    dic = {}
    name=str(input("请输入名字：　"))
    sex=str(input("请输入性别：　"))
    age=int(input("请输入年龄：　"))
    dic['name']=name
    dic['sex']=sex
    dic['age']=age
    list01.append(dic)
print(list01)


# rpc=('石头','剪刀','布')
# win=(('石头','剪刀'),('剪刀','布'),('布','石头'))
# import random
# while True:
#     ran=random.randint(0,2)
#     get=str(input("输入石头剪刀布"))
#     if (get,rpc[ran]) in win:
#         print("赢了")
#     elif(rpc[ran], get) in win:
#         print("输了")
#     elif get=='e':
#         break
#     else:
#         print("平手")
#
#
#
# """
#     字典推导式
#
# """
#
# # ｋｅｙ：数字　　　ｖａｌｕｅ：数字平方
# # dic01 = {}
# # for item in range(1,10):
# #     dic01[item] = item ** 2
# #
# # print(dic01)
# #
# # dic01 = {item:item ** 2 for item in range(1,10)}
#
# # dic01 = {}
# # for item in range(1, 100):
# #     if item % 2 == 0:
# #         dic01[item] = item ** 2
# #
# # dic01 = {item: item ** 2 for item in range(1, 100) if item % 2 == 0}
# # print(dic01)
#
#







