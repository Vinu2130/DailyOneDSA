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
    def traversal(self, node : Node):
        current = node 
        while current: 
            print(f"{current.data} -> ", end = "")
            current = current.next
        print("None")

# create single linked list : 0->1->2->3->4
head = Node(0)
temp = head
for i in range(1,5):
    temp.next = Node(i)
    temp = temp.next
# print(head.next.data)


sll = SinglyLinkedList(head)
sll.traversal(head)
    