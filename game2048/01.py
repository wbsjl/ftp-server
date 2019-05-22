
list01=[
    [0,0,0,2],
    [2,0,0,2],
    [2,2,4,2],
    [2,0,0,2],
]

class Controller:
    def move_zero(self,list01):
        for t in range(len(list01)-1):
            for num in range(len(list01)-1):
                if list01[num]==0:
                    list01[num],list01[num+1]=list01[num+1],list01[num]



    def combine(self,list01):
        self.move_zero(Controller,list01)
        for i in range(len(list01)-1):
            if list01[i]==list01[i+1]:
                list01[i]=list01[i]*2
                list01[i+1]=0
        self.move_zero(Controller,list01)

    def make_form(self,list01):
        for r in range(len(list01)):
            for c in range(len(list01[r])):
                print(list01[r][c], end="")
            print()



    def shift_left(self,list01):

        for i in range(len(list01)):
         self.combine(Controller,list01[i])
        for r in range(len(list01)):
            for c in range(len(list01[r])):
                print(list01[r][c],  end="")
            print()


    def shift_right(self,list01):

        for i in range(len(list01)):
            shift_right_list=list01[i][::-1]
            self.combine(Controller,shift_right_list)
            list01[i][::-1]=shift_right_list

        for r in range(len(list01)):
            for c in range(len(list01[r])):
                print(list01[r][c],  end="")
            print()







    # 定义向上的函数
    # 定义向下的函数






    def move_up(self,list01):
        for c in range(4):
            list_combine=[]
            for r in range(4):
                list_combine.append(list01[r][c])
            self.combine(Controller,list_combine)
            for r in range(4):
                list01[r][c]=list_combine[r]
        self.make_form(Controller,list01)



    def move_down(self,list01):
        for c in range(4):
            list_combine=[]
            for r in range(3,-1,-1):
                list_combine.append(list01[r][c])
            self.combine(Controller,list_combine)
            for r in range(3,-1,-1):
                list01[r][c]=list_combine[3-r]
        self.make_form(Controller,list01)


# def pop_num(list01):



while True:
    get_direction = str(input("direction: "))
    if get_direction=="w":
        Controller.move_up(Controller,list01)
    if get_direction=="a":
        Controller.shift_left(Controller,list01)
    if get_direction=="s":
        Controller.move_down(Controller,list01)
    if get_direction=="d":
        Controller.shift_right(Controller,list01)
    if get_direction=="q":
        break



