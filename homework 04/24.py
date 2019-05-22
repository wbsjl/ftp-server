



class Enemy:

    def __init__(self,id,name,atk,hp,asp):
        self.id=id
        self.name=name
        self.atk=atk
        self.hp=hp
        self.asp=asp

list01=[
    Enemy(101,'a',10,0,4),
    Enemy(102,'bfs',19,10,7),
    Enemy(103,'sd',15,32,5),
    Enemy(104,'d',8,49,9),
    Enemy(105,'eawea',15,2,20),

]

#
#
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
# result=max(list01,key=lambda e:e.atk)#最值
# print(result.id)
#
# print("-------------------------------------------------------")
#
# for item in filter(lambda i: 10<i.hp<50,list01):
#     print(item.id)
# print("-------------------------------------------------------")
# for item in filter(lambda i: i.atk,list01):
#     print(item.id)
# print("-------------------------------------------------------")
for item in sorted(list01,key=lambda i: i.atk):
    print(item.atk)
print("-------------------------------------------------------")
long=max(list01,key=lambda i: len(i.name))
print(long.id)







