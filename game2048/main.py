from ui import *




if __name__=="__main__":
    view = Control()
    try:
        view.main()
    except AttributeError as a:
        print("byebye")