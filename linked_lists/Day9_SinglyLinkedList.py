# Date : 12/07/2025 
# Problem : Singly Linked List
# complexity : 
# 1 . Traversal - O(n)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self,head = None):
        self.head = head
        
    # Traversal Operations
    def traversal(self, node = None):
        node = node or self.head
        current = node 
        print("The given Singly linked list is: ")
        while current: 
            print(f"{current.data} -> ", end = "")
            current = current.next
        print("None")
    def searchElement(self):
        k = int(input("Enter Search element : "))
        current = self.head
        while current:
            if current.data == k:
                print(f"Search Element {k} found in given singly linked list")
                return
            current = current.next
        print(f"Search Element {k} is not present in given singly linked list")
    def countElements(self):
        count = 0
        current  = self.head
        # print("The given Singly linked list is: ")
        while current: 
            # print(f"{current.data} -> ", end = "")
            count += 1
            current = current.next
        # print("None")
        # print(f"Total Number of elements in given singly linked list : {count}")
        return count
        
    # Insertion Operations
    def insertAtBeginning(self,k):
        newNode = Node(k)
        newNode.next = self.head
        self.head = newNode
        return self.head
    
    def insertAtEnd(self,k):
        newNode = Node(k)
        if self.head == None:
            self.head = newNode
            return self.head
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        return self.head
    
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
        temp = self.head
        while count < pos:
            # print(temp.data, count)
            count += 1
            temp = temp.next
            
        newNode.next = temp.next
        temp.next = newNode
        # return self.head
    
    # Deletion Operations
    def deleteAtBeginning(self):
        # newNode = Node(k)
        if self.head == None:
            return f"There is no element present in given linkedlist"
        deletedNode = self.head
        self.head = self.head.next 
        deletedNode.next = None
      
        return deletedNode.data
    
    def deleteAtEnd(self):
        # newNode = Node(k)
        if self.head == None:
            return f"There is no element present in given linkedlist"
        elif self.head.next == None:
            deletedNode = self.head
            self.head = None
            return deletedNode.data
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        deletedNode = temp.next
        temp.next = None
        return deletedNode.data
    
    def deleteAtPosition(self, pos):
        # newNode = Node(k)
        noOfElements = self.countElements() 
        # print(noOfElements)
        if noOfElements == 0 or pos > noOfElements or pos <= 0:
            return f"None"    
   
        if pos==1 :
            return self.deleteAtBeginning()
            
       
        elif pos == noOfElements:
            return self.deleteAtEnd()
       
        
        count = 2
        temp = self.head
        while count < pos:
            # print(temp.data, count)
            count += 1
            temp = temp.next
        deletedNode = temp.next 
        temp.next = temp.next.next
       
        return deletedNode.data
    
    # Modify element
    def updateAtPosition(self,pos,k):
        noOfElements = self.countElements() 
        # print(pos,k)
        if noOfElements == 0 or pos > noOfElements or pos <= 0:
            print(f"invalid position for updation: {pos}"  )
            return
        count = 1
        temp = self.head
        # print(self.head)
        while count!=pos:
            # print(temp.data)
            temp = temp.next
            count+=1
            
        temp.data = k
    
    # Reverse SLL
    def reverseSLL(self):
        prev = None
        temp = self.head
        # self.head.next = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        
        self.head = prev
            

# create single linked list : 0->1->2->3->4
head = Node(0)
temp = head
for i in range(1,5):
    temp.next = Node(i)
    temp = temp.next
# print(head.next.data)


sll = SinglyLinkedList(head)
# sll = SinglyLinkedList()
# sll.traversal()
# # sll.searchElement(3)
# sll.searchElement()
# sll.countElements()
sll.insertAtBeginning(5)
sll.insertAtBeginning(6)
sll.insertAtBeginning(7)
sll.insertAtEnd(8)
sll.insertAtPostion(10,10)
sll.traversal()
# print(sll.countElements())
# pos = 2

# print(f"Delete Node at position {pos}: {sll.deleteAtPosition(pos)}")
# print("updating position {pos} with {newData}: ")
# sll.updateAtPosition(32,21)
sll.reverseSLL()
sll.traversal()
    