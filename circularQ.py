class MyCircularQueue:
    def printQ(self):
      print("q = {}".format(self.q))
      print("size = {}".format(self.size))
      print("front = {}".format(self.front))
      print("rear = {}".format(self.rear))

    def __init__(self, k: int):
      self.size = k
      self.q = [None] * k
      self.front = self.rear = -1   # Front and rear indexes

    def enQueue(self, value: int) -> bool:
      if self.rear == -1:        
        self.rear = 0
        self.front = 0
        self.q[self.rear] = value
        return True
      
      temp = self.rear
      self.rear = (self.rear + 1) % self.size
      if self.rear == self.front:
        self.rear = temp
        return False
      
      self.q[self.rear] = value
      return True

    def deQueue(self) -> bool:
      if self.front == -1:
        return False
      
      if self.front == self.rear:
        self.front = self.rear = -1
        return True
      
      self.front = (self.front + 1) % self.size
      return True


    def Front(self) -> int:
      if self.front == -1:
        return -1
      else:
        return self.q[self.front]

    def Rear(self) -> int:
      if self.rear == -1:
        return -1
      else:
        return self.q[self.rear]

    def isEmpty(self) -> bool:
      return self.front == -1

    def isFull(self) -> bool:      
      return (self.rear + 1) % self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)

print("*************")
print("obj.enQueue(1)")
param_1 = obj.enQueue(1)
print(param_1)
obj.printQ()

print("*************")
print("obj.enQueue(2)")
param_1 = obj.enQueue(2)
print(param_1)
obj.printQ()

print("*************")
print("obj.enQueue(3)")
param_1 = obj.enQueue(3)
print(param_1)
obj.printQ()

print("*************")
print("obj.enQueue(4)")
param_1 = obj.enQueue(4)
print(param_1)
obj.printQ()

print("*************")
print("obj.Rear()")
param_4 = obj.Rear()
print(param_4)
obj.printQ()

print("*************")
print("obj.isFull()")
param_6 = obj.isFull()
print(param_6)
obj.printQ()

print("*************")
print("obj.deQueue()")
param_2 = obj.deQueue()
print(param_2)
obj.printQ()

print("*************")
print("obj.enQueue(4)")
param_1 = obj.enQueue(4)
print(param_1)
obj.printQ()

print("*************")
print("obj.Front()")
param_3 = obj.Front()
print(param_3)
obj.printQ()

print("*************")
print("obj.Rear()")
param_4 = obj.Rear()
print(param_4)
obj.printQ()

print("*************")
print("obj.deQueue()")
param_2 = obj.deQueue()
print(param_2)
obj.printQ()

print("*************")
print("obj.deQueue()")
param_2 = obj.deQueue()
print(param_2)
obj.printQ()

print("*************")
print("obj.deQueue()")
param_2 = obj.deQueue()
print(param_2)
obj.printQ()


print("*************")
print("obj.isEmpty()")
param_5 = obj.isEmpty()
print(param_5)
obj.printQ()

