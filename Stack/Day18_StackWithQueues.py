# (Implementing all the skipped tasks)
# Date : 29/07/2025
# Problem :  Implementation of Stack with queues

class CustomStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
    def push(self,k):
        if len(self.q1) == 0:
            self.q1.append(k)  
        else:
            self.q2.append(k)
            for i in self.q1:
                    self.q2.append(i)
            self.q1,self.q2 = self.q2,self.q1
            self.q2 = []
            
    def pull(self):
        self.q1.remove(self.q1[0])
    def top(self):
        return self.q1[0]
    def is_empty(self):
        return (len(self.q1)) == 0
    def displayQStack(self):
        # print(self.top)
        # print(self.is_empty())
        if self.is_empty():
            print("|_____|")
            return
        else:    
            for i in range(len(self.q1)):
                print(f"| {self.q1[i]} |")
            print("-----")
            
QStack = CustomStack()
print("Inserting : a")
QStack.push("a")
QStack.displayQStack()
print("Inserting : b")
QStack.push("b")
QStack.displayQStack()
print("Inserting : c")
QStack.push("c")
QStack.displayQStack()
print("Inserting : d")
QStack.push("d")
QStack.displayQStack()
print("Inserting : e")
QStack.push("e")
QStack.displayQStack()

print(QStack.top())

print("Delete top ")
QStack.pull()
QStack.displayQStack()
print("Delete top ")
QStack.pull()
QStack.displayQStack()
print("Delete top ")
QStack.pull()
QStack.displayQStack()
print("Delete top ")
QStack.pull()
QStack.displayQStack()
print("Delete top ")
QStack.pull()
QStack.displayQStack()
