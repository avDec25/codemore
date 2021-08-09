class Node:
  def __init__(self, key=-1, val=-1, next=None):
    self.key = key
    self.val = val
    self.next = next

class MyHashMap:
  
  def __init__(self):
    # using first node as the dummy node, chaining
    self.data = [Node() for _ in range(1000)]
        
  def hashcode(self, key):
    size = len(self.data)
    return key % size

  def put(self, key: int, value: int) -> None:
    hashcode = self.hashcode(key)
    head = self.data[hashcode]
    while head.next:
      if head.next.key == key:  
        head.next.val = value   # perform value update
        return
      head = head.next
    head.next = Node(key, value)
        

  def get(self, key: int) -> int:
    hashcode = self.hashcode(key)
    head = self.data[hashcode]
    while head.next:
      if head.next.key == key:
        return head.next.val
      head = head.next
    return -1

  def remove(self, key: int) -> None:
    hashcode = self.hashcode(key)
    head = self.data[hashcode]
    while head.next:
      if head.next.key == key:
        head.next = head.next.next
        return
      head = head.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
