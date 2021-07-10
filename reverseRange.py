# Definition for singly-linked list.
from typing import List


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right: return head
    d = p = ListNode(None)
    p.next = head
    for _ in range(left-1): p = p.next

    tail = p.next
    for _ in range(right-left):
      temp = p.next
      p.next = tail.next
      tail.next = tail.next.next
      p.next.next = temp
    return d.next

