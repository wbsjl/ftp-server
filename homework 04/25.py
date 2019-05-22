# x=[[1]]*3
# x[0][0]=5
# print(x)


# def additional(function):
#     def secure(check,*args,**kwargs):
#         print('新功能')
#         if check=='yes':
#             print(function.__name__)
#             return function(*args,**kwargs)
#         else:
#             print("no")
#     return secure
#
#
# @additional
# def enter_background(loginId,pwd):
#     print(loginId,pwd)
#     print("进入后台系统")
#
#
# @additional
# def delete_order(order_id):
#     print("删除%d订单..."%order_id)
#
#
# delete_order('yes',1234)




# def confirm(function):
#     def check(*args,**kwargs):
#         confirmation=int(input("输入验证码："))
#         if confirmation==100:
#             return function(*args,**kwargs)
#         else:
#             print('no')
#     return check
#
#
#
#
# @confirm
# def deposit(money):
#     print("存款",money)
#
#
# @confirm
# def withdraw():
#     print("取钱")
#     return 100000
#
# deposit(5000)
# print(withdraw())


import time

def count(function):
    def get_time(*args,**kwargs):
        start=time.time()
        result=function(*args, **kwargs)
        execute=time.time()-start
        print(execute)
        return result
    print(time.localtime())

    return get_time





class Student:
    def __init__(self,name):
        self.name=name
    @count
    def study(self):
        print("开始学习咯")
        time.sleep(2)






Student.study(time.time())






