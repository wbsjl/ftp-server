class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):

        print(self.val, self.next)


class LinkList:
    def __init__(self):
        self.head = None

    def init_list(self, l):
        self.head = Node(None)
        p = self.head

        for i in l:
            p. next = Node(i)
            p = p. next

    def show(self):

        p = self.head.next
        while p != None :
                print(p.val, end=" ")
                p = p.next
        print()

    # def add(self,i,l):
    #     l.append(i)
    #     self.init_list(l)

    def add(self,item):
        p=self.head
        while p.next is not None:
            p=p.next
        p.next = Node(item)


    def get_length(self):
        n=0
        p= self.head
        while p.next is not None:
            n+=1
            p = p.next
        return n

    def is_empty(self):
        if self.get_length()==0:
            return True
        return False

    def clear(self):
        self.head.next = None


    def get_item(self,i):
        list02=[]
        p = self.head
        while p.next is not None:
            p = p.next
            list02.append(p.val)
        if i>len(list02)-1:
            raise IndexError("list index out of range")
        print(str(list02[i]))


    def insert(self,index,item):
        if index < 0 or index> self.get_length():
            raise IndexError("list index out of range")
        p= self.head
        i=0
        while i<index:
            p=p.next
            i+=1
        node =Node(item)
        node.next=p.next
        p.next=node

    def delete(self,item):
        p= self.head
        while p.next is not None:
            if p.next.val == item:
                p.next = p.next.next
                break
            p= p.next
        else:
            raise ValueError("x not in list")



#
if __name__ == "__main__":
    print("Hello, earth")
    link = LinkList()
    list01 = [1, 2, 3, 4, 5, 6]
    link.init_list(list01)
    link.show()
    link.add(7)
    link.delete(3)
    link.insert(4,2)
    link.show()
    link.get_item(5)
    # print(link.head.val)
    # print(link.get_length())
    # print(link.is_empty())
    # link.clear()
    # print(link.get_length())
    # print(link.is_empty())


