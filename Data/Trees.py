from List import *
class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class Bittree:
    def __init__(self,root):
        self.root=root
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False


    def preOrder(self,node):
        if node is None:
            return
        print(node.data,end=' ')
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node is None:
            return

        self.preOrder(node.left)
        print(node.data, end=' ')
        self.preOrder(node.right)

    def postOrder(self, node):
        if node is None:
            return

        self.preOrder(node.left)
        self.preOrder(node.right)
        print(node.data, end=' ')

    def levelOrder(self,node):
        qu = Squeue()
        qu.enqueue(node)
        while not qu.is_empty():
            node = qu.dequeue()
            print(node.data,end =" ")
            if node.left:
                qu.enqueue(node.left)
            if node.right:
                qu.enqueue(node.right)





if __name__=="__main__":
    b= TreeNode('B')
    h = TreeNode('H')
    d = TreeNode('D')
    i = TreeNode('I')
    e = TreeNode('E',i,h)
    c = TreeNode('C',d,e)
    a = TreeNode('A',b,c)
    bt=Bittree(a)
    print("preorder:")
    bt.inOrder(a)
    bt.levelOrder(a)



