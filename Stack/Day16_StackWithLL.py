# (Implementing all the skipped tasks in weekend)
# Date : 26/07/2025
# Problem : Stack

# Dynamic Stack Implementation with Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL_Stack:
    def __init__(self,Peek = None):
        self.Peek = Peek
        self.top = -1
    
    def push(self,k):
        newNode = Node(k)
        if self.is_empty():
            self.Peek = newNode
            self.top += 1
            return
        newNode.next = self.Peek
        self.Peek= newNode
        self.top += 1
        
    def pop(self):
        if self.is_empty():
            return f"Stack is Empty"
        
        # elif self.Peek.next == None:
        #     deletedNode = self.Peek
        #     self.Peek = None
        #     self.top -= 1
        #     return deletedNode.data
        deletedNode = self.Peek
        self.Peek = self.Peek.next
        self.top -= 1
        return deletedNode.data
    def is_empty(self):
        return self.top == -1
    def displayStack(self):
        # print(self.top)
        # print(self.is_empty())
        if self.is_empty():
            print("|_____|")
            return
        temp = self.Peek
        while temp:
            print(f"| {temp.data} |")
            temp = temp.next
            
        print("-----")
    def getPeek(self):
        return self.Peek.data
    
s1 = LL_Stack()
s1.displayStack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)
s1.displayStack()
print(f"Deleted : {s1.pop()}")
print(f"Deleted : {s1.pop()}")
print(f"Deleted : {s1.pop()}")

s1.displayStack()
print(f"Deleted : {s1.pop()}")
print(f"Deleted : {s1.pop()}")
print(s1.top)
s1.displayStack()
print(s1.getPeek())
print(f"Deleted : {s1.pop()}")
print(s1.top)
print(f"Deleted : {s1.pop()}")
print(s1.top)
