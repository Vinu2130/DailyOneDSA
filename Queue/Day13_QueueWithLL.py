# (Implementing all the skipped tasks in weekend)
# Date : 26/07/2025
# Problem :  Linked List Implementation of Queue

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL_Queue:
    def __init__(self,Node = None):
        self.Node = Node
        self.front = None
        self.rear = None
    
    def Enqueue(self,k):
        newNode = Node(k)
        if self.front == None:
            self.front = newNode
            self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode
        
    def Dequeue(self):
        if self.front == None:
            return f"Queue is Empty"
        elif self.front == self.rear:
            deletedNode = self.front
            self.front = None
            self.rear = None
            return deletedNode.data
        deletedNode = self.front
        self.front = self.front.next
        return deletedNode
    def displayQ(self):
        temp = self.front
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        # print(None)
        print()
        return
    
lq = LL_Queue()
lq.Enqueue(1)
lq.Enqueue(2)
lq.Enqueue(3)
lq.displayQ()
lq.Dequeue()
lq.Dequeue()
lq.Enqueue(4)
lq.displayQ()

        