# (Implementing all the skipped tasks)
# Date : 29/07/2025
# Problem :  Implementation of Queue with stacks

class CustomQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self,k):
        if len(self.stack1) == 0:
            self.stack1.insert(0,k)
        else:
            # print(len(self.stack1))
            self.stack1 ,self.stack2 = self.stack2,self.stack1
            self.stack1.append(k)
            for i in self.stack2:
                self.stack1.append(i)
            self.stack2 = []
            
            # for i in range(len(self.stack1)):
            #     print(self.stack1[i])
            #     self.stack2.append(self.stack1[i])
            #     self.stack1.remove(self.stack1[i])
            
            # self.stack1.insert(0,k)
            # for i in range(len(self.stack2)):
            #     self.stack1.append(self.stack2[i])
            #     self.stack2.remove(self.stack2[i])
    def dequeue(self):
        x = self.stack1[len(self.stack1)-1]
        del self.stack1[len(self.stack1)-1]
        return x
        
    def is_empty(self):
        return self.stack1 == []
    def displaySQueue(self):
        if self.is_empty():
            print("---")
            print()
            print("---")
            return
        else: 
            print("------"*len(self.stack1))   
            for i in range(len(self.stack1)-1,-1,-1):
                
                print(f" {self.stack1[i]} ",end = "  ")
            print()
            print("------"*len(self.stack1))
            
Squeue = CustomQueue()
print("Inserting : a")
Squeue.enqueue("a")
Squeue.displaySQueue()
print("Inserting : b")
Squeue.enqueue("b")
Squeue.displaySQueue()
print("Inserting : c")
Squeue.enqueue("c")
Squeue.displaySQueue()
print("Inserting : d")
Squeue.enqueue("d")
Squeue.displaySQueue()
print("Delete front")
Squeue.dequeue()
Squeue.displaySQueue()
print("Delete front")
Squeue.dequeue()
Squeue.displaySQueue()
print("Delete front")
Squeue.dequeue()
Squeue.displaySQueue()