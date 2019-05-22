
# set1=set()
# while True:
#     get=str(input("输入字符串：　"))
#     if get=='q':
#         for i in get:
#             print(set1)
#         break
#     else:
#         set1.add(get)

#
# mana=['曹操','刘备','孙权']
# teq=['曹操','刘备','张飞','关羽']
#
# set1=set(mana)&set(teq)
# print(set1)
# set2=set(mana)-set(teq)
# print(set2)
# set3=set(teq)-set(mana)
# print(set3)
# print("张飞"in mana==True)
# set4=set(mana)^set(teq)
# print(set4)
# set5=set(mana)|set(teq)
# print(len(set5))
#


# for r in range(2):
#     for c in range(6):
#         print("*",end="")
#     print()
#     for c in range(6):
#         print("#",end="")
#     print()

# for r in range(4):
#     for c in range(r+1):
#         print("#",end="")
#     print()


# for r in range(4):
#     for c in range(r):
#         print(" ",end="")
#     for c in range(4-r):
#         print("#",end="")
#
#     print()

# list01=[1,4,7,4,8,0,6]
# for i in range(len(list01)-1):
#     for n in range(i+1,len(list01)):
#         if list01[i]==list01[n]:
#                 state=True
#                 break
#     if state==True:
#      break
# if state==True:
#     print("same")
# else:
#     print("dif")


# list01=[1,4,7,4,8,0,6]
# for i in range(len(list01)-1):
#
#     for n in range(i+1,len(list01)):
#         if list01[i]<list01[n]:
#             list01[i],list01[n]=list01[n],list01[i]
# print(list01)


# listf=["香蕉","苹果","哈密瓜"]
# listd=["可乐","牛奶"]
# list03=[r+c for r in listf for c in listd]
# print(list03)
#
# list3=[]
# for r in listf:
#     for c in listd:
#         list3.append(r+c)
# print(list3)

# n=int(input("enter"))
# def biu (n):
#
#     for i in range(n):
#         print("sad")
#
# biu(n)
#
# row=int(input("请输入行：　"))
# column=int(input("请输入列："))
# char=str(input("输入符号：　"))
# def draw (row,column,char):
#
#     for r in range(row):
#         for c in range(column):
#             print(char,end="")
#         print()
#
# draw(row,column,char)

# row=int(input("输入行"))
# char=str(input("输入符号：　"))
# def draw_triangle(row,char):
#     """
#     打印三角形
#     :param row: 三角形行数
#     :param char: 组成的字符
#     :return: void
#     """
#     for r in range(row):
#         for c in range(r+1):
#             print(char,end="")
#         print()
# draw_triangle(row,char    )





#
# list01=[1,4,7,4,8,0,6]
# def judge(list01):
#     for i in range(len(list01)-1):
#         for n in range(i+1,len(list01)):
#             if list01[i]==list01[n]:
#
#                 return True
#             else:
#                 return False
#
# re=judge(list01)


#
# getMonths=int(input("输入一个月份：　"))
# def find_seasons(getMonths):
#     if 1<=getMonths<=3:
#        return("春")
#     if 4<=getMonths<=6:
#        return("夏")
#     if 7<=getMonths<=9:
#        return("秋")
#     if 8<getMonths<=12:
#        return("冬")
#        return("请输入１～１２中的一个")
#
#
# print(find_seasons(getMonths))

# １判断奇数
# ２定义根据月份返回天数，２月如果是闰年返回２９，不然２８
# ３定义最小值
# ４定义函数，判断字符串中存在的中文字符数(0x4E00-0X9FA5)
# ５定义函数，返回范围内的素数



# getNum=int(input("输入一个数：　"))
#
# def judge(getNum):
#     if getNum%2:
#         return"奇数"
#     else:
#         return"偶数"
#
# print(judge(getNum))

# th1=(1,3,5,7,8,10,12)
# th0=(4,6,9,11)
# def get_days(th1,th0,getMonths,leapYear):
#     if getMonths in th1:
#        return 31
#     if getMonths in th0:
#        return 30
#     if getMonths==2:
#         if not leapYear%4 and leapYear%100 or(leapYear%400==0):
#             return(29)
#         else:
#             return 28
#     return 0
# print(get_days(th1,th0,13,2045))


# list1=[34,5,6,78,9,0,5,8,88,4]
# minN=list1[0]
# def find_min(list1,minN):
#     for i in range(1,len(list1)):
#         if minN>list1[i]:
#             minN=list1[i]
#     return minN
#
#
# print(find_min(list1,minN))

# list01=[]
# def record(list01,getString):
#     for item in getString:
#         list01.append(item)
#     return list01
#
# list02=record(list01,"啊打算的")
#
# def check_char(list02):
#     count=0
#     for chars in range(len(list02)):
#         if  0x4E00<=ord(list02[chars])<=0X9FA5:
#             count=count+1
#     return count
#
# print(check_char(list02))


# list01=[]
#
# def record(list01,initial,final):
#     for Nums in range(initial,final+1):
#         list01.append(Nums)
#     return list01
# list02=record(list01,1,12)
#
# list03=[]
# def countNum(list02):
#     for i in range(len(list02)):
#         if list02[i]<2:
#            list02[i]=" "
#         else:
#            for number in range(2, list02[i]-1,1):
#               if list02[i]%number==0:
#                  break
#            else:
#                  list03.append(list02[i])
#     return (list03)
# print(countNum(list02))





















