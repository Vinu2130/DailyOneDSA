# (Implementing all the skipped tasks in weekend)
# Date : 26/07/2025
# Problem : Stack

'''
Stack follows LIFO (Last In First Out) Principle so the element which is pushed last is popped first.
'''

# Fixed Stack Implementation with Array

class Stack:
    def __init__(self,capacity):
        if capacity <= 0:
            raise ValueError("Stack capacity must be greater than 0")

        self.s = [0] * capacity
        self.capacity = capacity
        self.top = -1
    def push(self,k):
        if self.top == self.capacity - 1:
            return f"Stack overFlow"
        self.top += 1
        self.s[self.top] = k
       
    def pop(self):
        if self.top == -1:
            return f"Stack underFlow"
        removed = self.s[self.top]
        self.top -= 1
        return removed
        
    def peek(self):
        if self.top == -1:
            return f"Stack is empty"

        return self.s[self.top]
    def is_empty(self):
        return self.top == -1
    def displayStack(self):
        # print(self.top)
        print(self.is_empty())
        if self.is_empty():
            print("|_____|")
            return
        else:    
            for i in range(self.top,-1,-1):
                print(f"| {self.s[i]} |")
            print("-----")
s1 = Stack(5)
print(s1.top)
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
print(s1.push(6))
s1.displayStack()
print(f"Deleted : {s1.pop()}")

print(f"Deleted : {s1.pop()}")
print(f"Deleted : {s1.pop()}")

s1.displayStack()
print(f"Deleted : {s1.pop()}")
print(f"Deleted : {s1.pop()}")
print(s1.top)
s1.displayStack()
print(s1.s)
print(s1.peek())

    
