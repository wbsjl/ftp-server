
def get():
     while True:
        try:
            getgrade=int(input("输入成绩"))



        except Exception as a:
                print("错")

        if 0<=getgrade<=100:
             return getgrade

        else:
             print("0-100")



print(get())