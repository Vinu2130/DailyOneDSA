# (Implementing all the skipped tasks in weekend)
# Date : 26/07/2025
# Problem :  Circular Array Implementation of Queue

'''
enqueue : insert into queue, (assume push),complexity is O(1)
dequeue : remove from queue, (assume pull),complexity is O(1)

Limitation :
* fixed capacity and only recent data can be stored
'''

class CircularQueue:
    def __init__(self, capacity):
        self.Cqueue = [0]*capacity
        self.front = 0
        self.capacity = capacity
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def getFront(self):
        return None if self.is_empty() else self.Cqueue[self.front]
    
    def getRear(self):
        return None if self.is_empty() else self.Cqueue[ (self.front +self.size -1) % self.capacity]
    
    def push(self, k):
        if self.size == self.capacity:
            return f"Queue is Full"
        rear = (self.front +self.size) % self.capacity
        self.Cqueue[rear] = k
        self.size += 1
        return f"{k} added to queue"
    def pull(self):
        if self.size == 0:
            return f"Queue is Empty"
        deletedElement = self.Cqueue[self.front]
        self.Cqueue[self.front] = 0
        self.front = (self.front+1)%self.capacity
        self.size -= 1
        return deletedElement
    

q1 = CircularQueue(5)
print(q1.Cqueue)
q1.push(1)
q1.push(2)
q1.push(3)
q1.push(4)
q1.push(5)
print(q1.getFront())
print(q1.getRear())
q1.push(6)
print(q1.Cqueue)
print(q1.pull())
print(q1.pull())
q1.push(7)
q1.push(8)
print(q1.Cqueue)
print(q1.pull())
print(q1.pull())
print(q1.pull())
print(q1.Cqueue)
q1.push(4)
q1.push(5)
q1.push(6)
print(q1.Cqueue)
print(q1.pull())
print(q1.pull())
print(q1.Cqueue)
print(q1.getFront())
print(q1.getRear())
print(q1.is_empty()) 
print(q1.pull())
print(q1.pull())
print(q1.pull())   
print(q1.pull())    
print(q1.is_empty())  
    