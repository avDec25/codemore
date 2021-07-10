from typing import List

class Node(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.total = 0
    self.left = None
    self.right = None

class SegmentTree(object):
  def __init__(self, nums):
    def createTree(nums, li, ri) -> Node:
      if li > ri:
        return None
      
      if li == ri:
        root = Node(li, ri)
        root.total = nums[li]
        return root
      
      mid = (li + ri) // 2
      root = Node(li, ri)
      root.left  = createTree(nums, li, mid)
      root.right = createTree(nums, mid+1, ri)
      root.total = root.left.total + root.right.total
      return root

    self.root = createTree(nums, 0, len(nums)-1)


  def update(self, index, newValue):
    def updateVal(root, i, v):
      if root.start == root.end:
        root.total = v
        return v
      
      mid = (root.start + root.end) // 2
      if i <= mid:
        updateVal(root.left, i, v)
      else:
        updateVal(root.right, i, v)

      root.total = root.left.total + root.right.total
      return root.total

    return updateVal(self.root, index, newValue)


  def sumRange(self, left, right):
    def rangeSum(root, li, ri):
      if root.start == li and root.end == ri:
        return root.total
      
      mid = (root.start + root.end) // 2
      if ri <= mid:
        return rangeSum(root.left, li, ri)
      elif mid+1 <= li:
        return rangeSum(root.right, li, ri)
      else:
        return rangeSum(root.left, li, mid) + rangeSum(root.right, mid+1, ri)

    return rangeSum(self.root, left, right)



nums = [1, 3, 5]
numArray = SegmentTree(nums)
print(numArray.sumRange(0, 1))
print(numArray.update(1, 10))
print(numArray.sumRange(1, 2))
