# class Student:
#     def __init__(self, name, score):
#         self.__name__ = name
#         self.__score__ = score
#
#     def get_score(self):
#         return self.__score__
#
#     def get_name(self):
#         return self.__name__
#
#     def __str__(self):
#         return str("name:{} score:{}".format(self.__name__, self.__score__))
#
#
# if __name__ == "__main__":
#     examine_scores = {"google": 98, "facebook": 99, "baidu": 52, "alibaba": 80, "yahoo": 49,
#                       "IBM": 70, "android": 76, "apple": 99}
#     students = [Student(x, y) for x, y in examine_scores.items()]
#     for student in students:
#         print(student)
#     print("===" * 5)
#     # 注意sorted 会生成行序列 不会改变原来的值。
#     students = sorted(students, key=lambda student: student.get_score())
#     # # 或者这样 但是不建议 破坏了封装
#     # students = sorted(students, key=lambda student: student.__score__)
#     for student in students:
#         print(student)
# 自定义方法实现

# people={}
# for x in range(1,31):
#     people[x]=1
#
#
# # print(people)
# check=0
# i=1
# j=0
# while i<=31:
#     if i == 31:
#         i=1
#     elif j == 15:
#         break
#     else:
#         if people[i] == 0:
#             i+=1
#             continue
#         else:
#             check+=1
#             if check == 9:
#                 people[i]=0
#                 check = 0
#                 print("{}号下船了".format(i))
#                 j+=1
#             else:
#                 i+=1
#                 continue
# print(people)
#
# list01=[]
#
# for y in people.keys():
#         if people[y]!=0:
#             list01.append(y)
#
# print(list01)

# print("测试实例一")
# str = "runoob.com"
# print(str.isalnum()) # 判断所有字符都是数字或者字母
# print(str.isalpha()) # 判断所有字符都是字母
# print(str.isdigit()) # 判断所有字符都是数字
# print(str.islower()) # 判断所有字符都是小写
# print(str.isupper()) # 判断所有字符都是大写
# print(str.istitle()) # 判断所有单词都是首字母大写，像标题
# print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r









