# Date : 18/07/2025 
# Problem : Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self,head = None):
        self.head = head
    
    def traversal(self,node = None):
        node = node or self.head
        current = node 
        print("The given Doubly linked list is: ")
        while current: 
            print(f"{current.data} <-> ", end = "")
            current = current.next
        print("None")
    
    def countElements(self):
        count = 0
        current  = self.head
        while current:
            count += 1
            current = current.next
       
        return count
        
    def searchElement(self):
        k = int(input("Enter Search element : "))
        current = self.head
        while current:
            if current.data == k:
                print(f"Search Element {k} found in given Doubly linked list")
                return
            current = current.next
        print(f"Search Element {k} is not present in given Doubly linked list")
    
    # Insert operations
    def insertAtBeginning(self,k):
        newNode = Node(k)
        if self.head == None:
            self.head = newNode
            return self.head
        newNode.next = self.head
        self.head.prev = newNode
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
        newNode.prev = temp
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
        temp.next.prev = newNode
        temp.next = newNode
        newNode.prev = temp
        # return self.head
        
    # Deletion Operations
    def deleteAtBeginning(self):
        # newNode = Node(k)
        if self.head == None:
            return f"There is no element present in given linkedlist"
        deletedNode = self.head
        self.head = self.head.next 
        self.head.prev = None
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
        deletedNode.prev = None
        temp.next = None
        return deletedNode.data
    
    def deleteAtPosition(self, pos):
        noOfElements = self.countElements() 
        if noOfElements == 0 or pos > noOfElements or pos <= 0:
            return f"None"    
        if pos==1 :
            return self.deleteAtBeginning()
        elif pos == noOfElements:
            return self.deleteAtEnd()
        count = 2
        temp = self.head
        while count < pos:
            count += 1
            temp = temp.next
        deletedNode = temp.next 
        temp.next = temp.next.next
        temp.next.prev = temp
        return deletedNode.data
    
    def updateAtPosition(self,pos,k):
        noOfElements = self.countElements() 
        if noOfElements == 0 or pos > noOfElements or pos <= 0:
            print(f"invalid position for updation: {pos}"  )
            return
        count = 1
        temp = self.head
        while count!=pos:
            temp = temp.next
            count+=1  
        temp.data = k
        
    def reverseDLL(self):
        left = None
        temp = self.head
        
        while temp:
            right = temp.next
            temp.next = left
            temp.prev = right
            left = temp
            temp = right
        
        self.head = left
    

    
   
        
        
    
head = Node(5)
dll = DoublyLinkedList(head)
for i in range(5):
    dll.insertAtBeginning(i)
dll.insertAtEnd(7)
dll.insertAtPostion(6,7)
dll.traversal()
# print(dll.deleteAtBeginning())
dll.traversal()
# print(dll.deleteAtEnd())
dll.deleteAtEnd()


dll.traversal()
dll.deleteAtPosition(5)
dll.traversal()
dll.updateAtPosition(1,7)
dll.traversal()
dll.reverseDLL()
dll.traversal()
print(dll.countElements())
dll.searchElement()
         
        