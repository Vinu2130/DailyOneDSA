# Date : 21/07/2025 
# Problem : Queue

'''
Queue is a linear data structure that follows FIFO (First In First Out) Principle, so the first element inserted is the first to be popped out.

# elements addition should be done from front end and removal should be done from rear end

lets take index 0 as front and last index as rear ends

enqueue : insert into queue, (assume push),complexity is O(1)
dequeue : remove from queue, (assume pull),complexity is O(n)
'''

# Simple Array Implementation Of Queue
class Queue:
    def __init__(self):
        self.q = [] 
    def push(self,k):
        self.q.append(k)       
    def pull(self):
        self.q.remove(self.q[0])
    def getHead(self):
        return self.q[0]
    def getTail(self):
        return self.q[len(self.q)-1]
    def is_empty(self):
        return (len(self.q)) == 0
    

q1 = Queue()
print(q1.q)
q1.push(1)
q1.push(2)
q1.push(3)
print(q1.q)
print(q1.getHead())
q1.pull()
print(q1.q)
print(q1.getHead())
print(q1.getTail())
print(q1.is_empty())