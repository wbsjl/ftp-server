import random
import copy
from model import*
import os

list02 = [
    [0]*4,
    [0]*4,
    [0]*4,
    [0]*4,
]


class Controller:
    


    def __move_zero(self, list01):
        for t in range(len(list01) - 1):
            for num in range(len(list01) - 1):
                if list01[num] == 0:
                    list01[num], list01[num + 1] = list01[num + 1], list01[num]

    def __combine(self, list01):
        self.__move_zero(self, list01)
        for i in range(len(list01) - 1):
            if list01[i] == list01[i + 1]:
                list01[i] = list01[i] * 2
                list01[i + 1] = 0
        self.__move_zero(Controller, list01)

    def make_form(self, list01):
        os.system("clear")
        for r in range(len(list01)):
            for c in range(len(list01[r])):
                print(list01[r][c], end="\t")
            print()
            print()

    def __shift_left(self, list01):
        list03 = copy.deepcopy(list02)
        for i in range(len(list01)):
            self.__combine(Controller, list01[i])
            if list01 != list03:
                Controller.make_new_numbers(Controller,list01)
                # for r in range(len(list01)):
                #     for c in range(len(list01[r])):
                #         print(list01[r][c],  end="")
                #     # print()

    def __shift_right(self, list01):
        list03 = copy.deepcopy(list01)

        for i in range(len(list01)):
            shift_right_list = list01[i][::-1]
            self.__combine(Controller, shift_right_list)
            list01[i][::-1] = shift_right_list
        if list01 != list03:
            Controller.make_new_numbers(Controller, list01)



            # for r in range(len(list01)):
            #     for c in range(len(list01[r])):
            #         print(list01[r][c],  end="")
            #     # print()

    # 定义向上的函数
    # 定义向下的函数

    def __move_up(self, list01):

        list03 = copy.deepcopy(list01)

        for c in range(4):
            list_combine = []
            for r in range(4):
                list_combine.append(list01[r][c])
            self.__combine(Controller, list_combine)
            for r in range(4):
                list01[r][c] = list_combine[r]
        if list01 != list03:
            Controller.make_new_numbers(Controller, list01)
            # self.make_form(Controller,list01)

    def __move_down(self, list01):
        list03 = copy.deepcopy(list01)
        for c in range(4):
            list_combine = []
            for r in range(3, -1, -1):
                list_combine.append(list01[r][c])
            self.__combine(Controller, list_combine)
            for r in range(3, -1, -1):
                list01[r][c] = list_combine[3 - r]
        if list01 != list03:
            Controller.make_new_numbers(Controller, list01)
            # self.make_form(Controller,list01)



    def move(self, dir):
        """
            移动
        :param dir: Direction类型　
        :return:
        """
        # 假设没有发生变化

        # 通过深拷贝(二维列表)记录移动前的地图　

        if dir == Direction.up:
            self.__move_up(Controller, list02)
        elif dir == Direction.down:
            self.__move_down(Controller, list02)
        elif dir == Direction.left:
            self.__shift_left(Controller, list02)
        elif dir == Direction.right:
            self.__shift_right(Controller, list02)


    def check_fill(self, list01):
        # list05 = copy.deepcopy(list01)
        # self.__shift_left(Controller, list05)
        # if list05 == list01:
        #     self.__shift_right(Controller, list05)
        #
        # if list05 == list01:
        #     self.__move_up(Controller, list05)
        #
        # if list05 == list01:
        #     self.__move_down(Controller, list05)
        #
        # if list05 == list01:
        #     print("gameover")
        #     return True
        list04=[]
        for r in range(len(list01)-1):
            for c in range(len(list01[r])-1):
                list04.append(list01[r][c])
                if list01[r][c]==list01[r][c+1] or list01[r][c]==list01[r+1][c]:
                    return False
                if 0 in list04:
                    return False
        print("gameover")
        return True

    def make_new_numbers(self, list01):

        random_select = random.randint(1, 10)
        if random_select == 1:
            random_number = 4
        else:
            random_number = 2
        while True:
            random_x = random.randint(0, 3)
            random_y = random.randint(0, 3)
            list04 = []
            for r in range(len(list01)):
                for c in range(len(list01[r])):
                    list04.append(list01[r][c])
            if 0 not in list04:
                break
            a = random_x
            b = random_y
            if list01[a][b] == 0:
                list01[a][b] = random_number
                break
            else:
                continue

#
# while True:
#     get_direction = str(input("direction: "))
#     if get_direction=="w":
#         Controller.__move_up(Controller,list02)
#         Controller.make_new_numbers(Controller,list02)
#     if get_direction=="a":
#         Controller.__shift_left(Controller,list02)
#         Controller.make_new_numbers(Controller, list02)
#
#     if get_direction=="s":
#         Controller.__move_down(Controller,list02)
#         Controller.make_new_numbers(Controller, list02)
#     if get_direction=="d":
#         Controller.__shift_right(Controller,list02)
#         Controller.make_new_numbers(Controller, list02)
#     if get_direction=="q":
#         break
