# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    i, j, c, ld = l1, l2, 0, 0
    root = None
    p = None
    while i and j:
      summed = c + i.val + j.val
      c, ld = divmod(summed, 10)
      if not root:
        root = ListNode(ld)
        p = root
      else:
        p.next = ListNode(ld)
        p = p.next
      i = i.next
      j = j.next
      
    
    while j:
      summed = c + j.val
      c, ld = divmod(summed, 10)
      p.next = ListNode(ld)
      p = p.next
      j = j.next

    
    while i:
      summed = c + i.val
      c, ld = divmod(summed, 10)
      p.next = ListNode(ld)
      p = p.next
      i = i.next

    if c != 0:
      p.next = ListNode(c)
      p = p.next

    return root


l1 = [2,4,9, 9]
l2 = [5,6]
p = Solution().addTwoNumbers(l1, l2)
while p:
  print(p.val)
  p = p.next