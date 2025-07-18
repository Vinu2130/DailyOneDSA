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
    def insertAtBeginning(self,k):
        newNode = Node(k)
        if self.head == None:
            self.head = newNode
            return self.head
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        return self.head
    def traversal(self,node = None):
        node = node or self.head
        current = node 
        print("The given Singly linked list is: ")
        while current: 
            print(f"{current.data} <-> ", end = "")
            current = current.next
        print("None")
        
        
    
head = Node(5)
dll = DoublyLinkedList(head)
for i in range(5):
    dll.insertAtBeginning(i)
dll.traversal()
    
        
        