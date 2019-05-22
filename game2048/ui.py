from GameCoreController import Controller,list02
from model import *



class Control:





    def __start(self):
        Controller.make_new_numbers(Controller, list02)
        Controller.make_new_numbers(Controller, list02)
        Controller.make_form(Controller, list02)

    def __move_up(self):
        Controller.move(Controller, Direction.up)
        Controller.make_form(Controller, list02)

    def __move_down(self):
        Controller.move(Controller, Direction.down)
        Controller.make_form(Controller, list02)

    def __move_right(self):
        Controller.move(Controller, Direction.right)
        Controller.make_form(Controller, list02)

    def __move_left(self):
        Controller.move(Controller, Direction.left)
        Controller.make_form(Controller, list02)



    def Run(self):

        self.__start(Control)

        while True:
            get_direction = str(input("direction: "))
            if get_direction == "w":
                Control.__move_up(Controller)
                if Controller.check_fill(Controller,list02):
                    break
            if get_direction == "a":
                Control.__move_left(Controller)
                if Controller.check_fill(Controller,list02):
                    break
            if get_direction == "s":
                Control.__move_down(Controller)
                if Controller.check_fill(Controller,list02):
                    break
            if get_direction == "d":
                Control.__move_right(Controller)
                if Controller.check_fill(Controller,list02):
                    break




Control.Run(Control)