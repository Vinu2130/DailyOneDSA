# Date : 21/07/2025 
# Problem : Queue

'''
Queue is a linear data structure that follows FIFO (First In First Out) Principle, so the first element inserted is the first to be popped out.
'''


class Queue:
    def __init__(self,arr):
        self.size = len(arr)
        if self.size == 0:
            self.front = None
            self.rear = None
        self.front = self.size - 1
        self.rear = 0
        
    def push(self,k):
        if self.front == None and self.rear == None:
            arr[0] = k
            self.front = k
            self.rear = k
        else:
            arr.append(k)
            self.front = k
    def pull(self):
        arr.remove(self.front)
        self.front = self.size - 1
        return self.front
    def getHead(self):
        return self.front
    def getTail(self):
        return self.rear
    

arr = [1,2,3,4,5]
q = Queue(arr)
q.push(6)
q.push(7)
q.push(8)
print(q.pull())
print(arr)
print(q.getHead())
print(q.getTail())