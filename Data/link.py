class StackError(Exception):
    pass

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LStack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top is None

    def push(self,elem):
       self.top = Node(elem,self.top)

    def pop(self):
        if self.top is None:
            raise StackError("empty")
        p= self.top
        self.top = p.next
        return p.val
    def top(self):
        if self.top is None:
            raise StackError("None")
        return self.top.val

    def Reverse_polish_notation(self,calculate):
        list01=[" ","+","-","*","/","%","//","**"]

        formula=calculate.split(" ")
        for i in formula:
            if i not in list01:
                self.push(i)
            elif i in list01:
                    a= eval(str(self.top.next.val) +i+str(self.top.val))
                    self.pop()
                    self.pop()
                    self.push(a)
            elif i=='p':
                break

        return self.top.next.val







if __name__ == "__main__":
    st = LStack()
    # print(st.is_empty())
    # st.push(50)
    # st.push(40)
    # st.push(30)
    # st.push(20)
    # while not st.is_empty():
    #     print(st.pop())
    print(st.Reverse_polish_notation("67 25 + 38 - p"))






