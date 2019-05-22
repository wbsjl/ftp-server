#
#
#getMonths=int(input("输入一个月份：　"))
#
#if 1<=getMonths<=3:
#    print("春")
#elif 4<=getMonths<=6:
#    print("夏")
#elif 7<=getMonths<=9:
#    print("秋")
#elif 8<getMonths<=12:
#    print("冬")
#else:
#    print("请输入１～１２中的一个")

#
# getSeason=str(input("输入一个季度　"))
#
# if getSeason=="春":
#    print("1,2,3")
# elif getSeason=="夏":
#    print("4,5,6")
# elif getSeason=="秋":
#    print("7,8,9")
# elif getSeason=="冬":
#    print("10,11,12")
# else:
#    print("输入季节")

#getMonths=int(input("请输入一个月份"))
#if getMonths==1 or  getMonths==3 or getMonths==5 or getMonths==7 or getMonths==8 or getMonths==10 or getMonths==12:
#    print("三十一天")
#elif getMonths==getMonths==4 or getMonths==6 or getMonths==9 or getMonths==11:
#    print("三十天")
#elif getMonths==2:
#    print("二十八天")
#else:
#    print("请输入月份１～１２")


#num1=int(input("输入一个数"))
#num2=int(input("输入一个数"))
#num3=int(input("输入一个数"))
#num4=int(input("输入一个数"))
#
#largest=num1
#
#if num2>num1:
#    largest=num2
#if num3>num1:
#    largest=num3
#if num4>num1:
#    largest=num4
#print(largest)
#

# getNum=int(input("输入一个数：　"))
# if getNum%2:
#    print("奇数")
# else:
#    print("偶数")
#
#leapYear=int(input("输入一个年份：　"))
#day=29 if not leapYear%4 and leapYear%100 or(leapYear%400==0) else 28
#print(day)
#

#num=int(input("输入一个数：　"))
#num2=int(input("输入结尾数"))
#x=num
#while num<=x<num2:
#    x+=1
#    print(x)




#thickness=0.00001
#times =0
#while thickness<8844.43:
#    thickness+=thickness
#    times+=1
#    print(thickness)
#
#print(times)
#

#import random
#
#randomNum= random.randint(1,100)
##while True:
#    guess = int(input("请输入一个数字：　"))
#    if guess==randomNum:
#        print("对了")
#        break
#    elif guess<randomNum:
#        print("小了")
#    else:
#        print("大了")
#
#chance=10
#while chance>0:
#    guess = int(input("请输入一个数字：　"))
#    if guess==randomNum:
#        print("对了"+str(chance))
#        break
#    elif guess<randomNum:
#        print("小了,还有："+str(chance-1))
#        chance-=1
#    else:
#        print("大了,还有:"+str(chance-1))
#        chance-=1
#else:
#    print("没机会了")
#


#for element in "niconiconi":
#    print(element)
#
#for element in range(1,12,1):
#    print(element)

#for element in range(5):
#    input1=input("输入第一个变量")
#    input2=input("输入第二个变量")
#    input1,input2=input2,input1
#    print(input1,input2)


#import random
#credits=0
#for element in range(5):
#    ram=random.randint(1,100)
#    ram2=random.randint(1,100)
#    print(ram,ram2)
#    answer=int(input("请输入它们的和：　"))
#    if answer==ram+ram2:
#        credits+=10
#        print("对了加十分")
#    else:
#        credits-=5
#        print("错了扣五分")
#else:
#    print("结束了"+str(credits)+"分")
#sum=0
#for number in range(1,101,1):
#    if number%3!=0:
#        continue
#    sum=sum+number
#    print(number,sum)

# height=100
# total=0
# jumps=0
# while height/2>=0.01:
#    height=height/2
#    jumps+=1
#    total=total+height
#
#    print(height)
# print(jumps)
# print(round(total*2+100,2))

# request=int(input("请输入一个数：　"))
# if request<2:
#    print("不是素数")
# else:
#
#    for number in range(2, request-1,1):
#       if request%number==0:
#          print("这不是个素数")
#          break
#    else:
#          print("这是个素数")
# # count=1
# for letters in 'biudadada':
#     getA=(input("enter a: "))
#     getB=(input("enter b: "))
#     compare=getA or getB
#     print(letters)
#     count+=1
#     if not compare:
#         continue
#     print(compare)

# print(ord('b'))
# print(chr(4396))
#

"""

"""
getStr=str(input("输入一个字符: "))
for value in getStr:
   print(ord(value))

while True:
   getCode=int(input("输入一个编码值"))
   if getCode<0:
      print("end")
      break
   else:
      print(chr(getCode))









