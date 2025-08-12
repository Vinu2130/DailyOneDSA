# Date : 26/07/2025
# Problem :  Simple Binary Tree

class Node:
    def __init__(self,v):
        self.data = v
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,data):
        self.root = Node(data)
    def insertLeft(self,parent:Node,child):
        parent.left = Node(child)
    def insertRight(self,parent:Node,child):
        parent.right= Node(child)
    
    def PreOrder(self,node):
        if node:
            print(node.data, end = " ")
            self.PreOrder(node.left)
            self.PreOrder(node.right)

      


myBT = BinaryTree(4)
myBT.insertLeft(myBT.root,3)
myBT.insertRight(myBT.root,5)
myBT.insertLeft(myBT.root.left,2)
myBT.PreOrder(myBT.root)



