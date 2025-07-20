# Date : 20/07/2025 
# Problem : Circular Linked List

'''
* A circular linked lists is a linked list in which last node is pointing towards head node instaed of Null.

We have two types of circular linked list :
1. single circular linked list
2. double circular linked list

(Here, we are going to implement only single circular linked list)
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self,last = None):
        self.last = last
        self.first = last
        
    def traversal(self,Node = None):
        if self.first is None:
            print("List is empty.")
            return

        Node = Node or self.first
        print(f"{Node.data}",end="")
        Node = Node.next
        while Node != self.first:
            print(f"->{Node.data}", end = "")
            Node = Node.next
        print(f"->{Node.data}")
        # print(f"{Node.data}")
        
    def countElements(self):
        count = 1
        if self.first is None:
            print("List is empty.")
            return count
        current  = self.first
        current = current.next
        while current != self.first: 
            count += 1
            current = current.next
        return count
        
    # insertion Operations
    def insertIntoEmptyList(self,k):
        newNode = Node(k)
        if self.first is None and self.last is None:
            self.first = newNode
            self.last = newNode
            newNode.next = self.first
    def insertAtBeginning(self,k):
        
        if self.first is None:
            self.insertIntoEmptyList(k)
            return
        newNode = Node(k)
        self.last.next = newNode
        newNode.next = self.first
       
        self.first = newNode
    
    def insertAtEnd(self,k):
        
        if self.first is None:
            self.insertIntoEmptyList(k)
            return
        newNode = Node(k)
        self.last.next = newNode
        newNode.next = self.first
       
        self.last = newNode
    
    def insertAtPostion(self,k,pos):
        newNode = Node(k)
        noOfElements = self.countElements() 
   
        if pos==1 :
            self.insertAtBeginning(k)
            return
       
        elif pos > noOfElements:
            self.insertAtEnd(k)
            return
        count = 2
        temp = self.first
        while count < pos:
            # print(temp.data, count)
            count += 1
            temp = temp.next
            
        newNode.next = temp.next
        temp.next = newNode
        
    
            
            
        
        
        

# last = Node(0)
# first = last
# for i in range(1,6):
#     last.next = Node(i)
#     last = last.next
# last.next = first

cll = CircularLinkedList()
cll.insertIntoEmptyList(0)
# cll.insertAtBeginning(1)
# cll.insertAtBeginning(2)
# cll.insertAtBeginning(3)
# cll.insertAtBeginning(9)
cll.insertAtBeginning(10)
cll.insertAtEnd(7)
cll.insertAtPostion(5,3)
print(cll.first.data)
cll.traversal()

    