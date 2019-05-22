# print(ord('b'))
# print(chr(4396))
#

"""
单引号与双引号功能相同，三引号表注释


"""
# getStr=str(input("输入一个字符: "))
# for value in getStr:
#    print(ord(value))
#
# while True:
#    getCode=int(input("输入一个编码值"))
#    if getCode<0:
#       print("end")
#       break
#    else:
#       print(chr(getCode))
#

# seconds=180
# minute=seconds/60
# sec=0
#
# while seconds>=0 and minute >=0:
#     print("%02d.:%02d."%(minute,sec))
#     if sec==0:
#         sec=sec+60
#     if sec==60:
#         minute-=1
#     sec-=1

# str1="abcdefg"
# print(str1[4])
# print(str1[len(str1)-1])
# print(str1[0:5])
# print(str1[-1:-4:-1])

# string=str(input("输入一个字符串"))
# print(string[0])
# print(string[len(string)-1])
# if len(string)%2!=0:
#     print(string[(len(string)-1)//2])
# print(string[-3:])
# print(string[::-1])
#
#
# side=int(input("输入边长：　"))
# print("*"*side)
# for long in range(side-2):
#     print("*"+" "*(side-2)+"*")
# print("*"*side)


# list1=list("niconiconi")
# print(list1)
# list2=["ni","co","ni","co","ni"]
# list2.append("nico")
# list2.insert(5,"!")
# list2.remove("nico")
# del list2[5]
# print(list2)

# population = int(input("请输入学生人数"))
# gradelist = []
# order = 1
# table = 0
# for student in range(population):
#     grade = int(input("请输入第" + str(order) + "个学生的成绩"))
#     gradelist.append(grade)
#     order += 1
# print(gradelist)
# print(max(gradelist))
# print(min(gradelist))
# print(sum(gradelist))

# Namelist=[]
# while True:
#     Names = str(input("请输入学生姓名"))
#
#     if Names in Namelist:
#         print("这个有了")
#         continue
#
#     if Names=="esc":
#
#         print("结束")
#
#         break
#     Namelist.append(Names)
# for i in Namelist:
#     print(i)


#
# list1=[34,5,6,78,9,0,5,8,88,4]
# minN=list1[0]
# for i in range(1,len(list1)):
#     if minN>list1[i]:
#         minN=list1[i]
# print(minN)
#
# list2=[]
# for item in range(10):
#     list2.append(str(item))
# result="-".join(list2)
# print(result)
#
# io="fjien#wefwe#wer"
# split1=io.split("#")
# print(split1)
#
# 循环录入字符串，按ｑ退出，然后显示新的字符串（合并之前的）
# 判断是否回文
# 一注彩票七个，六个红，一个蓝，红１－３３，不重复，蓝１－１６
# １．在控制台中购买彩票
# ２．随机生产一注彩票

# list01=[]
# while True:
#     string=str(input("输入字符串：　"))
#     if string=="q":
#         print("end")
#         break
#     list01.append(string)
# result=",".join(list01)
# print(result)


#
# string=str(input("输入字符串：　"))
# if string==string[::-1]:
#    print("回文")
# else:
#     print("不是回文")

# lottery=[]
# count=1
# for i in range(6):
#     getNum=str(input("请输入第"+str(count)+"个红球号码：　"))
#     while 1>int(getNum) or int(getNum)>33:
#         print("只能１－３３")
#         getNum = str(input("请输入第"+str(count)+"个红球号码：　"))
#     while getNum in lottery:
#         print("已经有了")
#         getNum = str(input("请输入第"+str(count)+"个红球号码：　"))
#     lottery.append(getNum)
#     count+=1
# getBNum=str(input("请输入一个蓝球号码：　"))
# while 1>int(getBNum) or int(getBNum)>16:
#     print("只能１－16")
#     getBNum = str(input("请输入一个蓝球号码：　"))
# lottery.append(getBNum)
# result="-".join(lottery)
#
# print(result)

# import random
# lottery=[]
# for i in range(6):
#     getNum=str(random.randint(1,33))
#     while getNum in lottery:
#         getNum = str(random.randint(1, 33))
#     lottery.append(getNum)
# lottery.sort()
# getBNum=str(random.randint(1,16))
# lottery.append(getBNum)
#
# result="-".join(lottery)
#
# print(result)


