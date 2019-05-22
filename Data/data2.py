class StackError(Exception):
    pass


class Sstack:
    def __init__(self):
        # 约定列表最后一个元素为栈顶元素
        self.elems = []

    def top(self):
        if not self.elems:
            raise StackError("no stack")
        return self.elems[-1]

    def is_empty(self):
        return self.elems == []

    def push(self,elem):
        self.elems.append(elem)

    def pop(self):
        if not self.elems:
            raise StackError("no stack")
        return self.elems.pop()

    # def detect(self,i):
    #     list02=[]
    #     list(i)
    #     for item in i:
    #         if item =="(":
    #             list02.append(item)
    #         if item ==")":
    #             out_one=list02.pop()
    #             if out_one!="(":
    #                 raise IndexError("wrong one")
    #             print("nice")



if __name__ == "__main__":
    st = Sstack()
    # print(st.top())
    print(st.is_empty())
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    while not st.is_empty():
        print(st.pop())

