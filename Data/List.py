class QueueError(Exception):
    pass


class Squeue:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def enqueue(self,elem):
        self.elems.append(elem)

    def dequeue(self):
        if not self.elems:
            raise QueueError("no")
        return self.elems.pop(0)

if __name__=="__main__":
    sq = Squeue()
    print(sq.is_empty())
    sq.enqueue(1)
    sq.enqueue(2)
    sq.enqueue(3)
    while not sq.is_empty():
        print(sq.dequeue())



