# class QueueError(Exception):
#     pass
#
# class Node:
#     def __init__(self,val,next=None):
#         self.next=next
#         self.val=val
#
# class Lsqueue:
#     def __init__(self):
#         self.last=self.first = Node(None)
#
#
#
#     def is_empty(self):
#         return self.first == self.last
#
#     def enqueue(self,elem):
#         self.last.next = Node(elem)
#         self.last = self.last.next
#
#
#     def dequeue(self):
#         if self.first == self.last:
#             raise QueueError("empty")
#         self.first = self.first.next
#         return self.first.val
#
# if __name__=="__main__":
#     sq = Lsqueue()
#     print(sq.is_empty())
#     sq.enqueue(1)
#     sq.enqueue(2)
#     sq.enqueue(3)
#     print(sq.is_empty())
#     while not sq.is_empty():
#         print(sq.dequeue())

def recursion(n):
    if n <=1:
        return 1
    return (n*recursion(n-1))

print(recursion(5))


