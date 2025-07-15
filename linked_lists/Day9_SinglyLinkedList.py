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
            print(temp.data, count)
            count += 1
            temp = temp.next
            
        newNode.next = temp.next
        temp.next = newNode
        return self.head
    
    
        
      
        
        

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
# sll.traversal()
# print(sll.countElements())
    