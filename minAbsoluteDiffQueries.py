from typing import List
import math

class Node(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.absDiff = math.inf
    self.left = None
    self.right = None

class SegmentTree(object):
  def __init__(self, nums):
    def createTree(nums, li, ri) -> Node:
      if li > ri:
        return None
      
      if li == ri:
        root = Node(li, ri)
        root.absDiff = nums[li]
        return root
      
      mid = (li + ri) // 2
      root = Node(li, ri)
      root.left  = createTree(nums, li, mid)
      root.right = createTree(nums, mid+1, ri)

      for i in range(root.left.start, root.left.end):
        root.left.absDiff = min(root.left.absDiff, abs(nums[i] - nums[i+1]))
      
      for i in range(root.right.start, root.right.end):
        root.right.absDiff = min(root.right.absDiff, abs(nums[i] - nums[i+1]))

      for i in range(root.left.start, root.right.end):
        root.absDiff = min(root.absDiff, abs(nums[i] - nums[i+1]))

      return root

    self.nums = nums
    self.root = createTree(nums, 0, len(nums)-1)


  def absDifference(self, left, right):
    def absoluteDiff(root, li, ri):
      if root.start == li and root.end == ri:
        return root.absDiff
      
      mid = (root.start + root.end) // 2
      if ri <= mid:
        return absoluteDiff(root.left, li, ri)
      elif mid+1 <= li:
        return absoluteDiff(root.right, li, ri)
      else:
        combined = math.inf
        for i in range(root.left.start, root.right.end):
          combined = min(combined, abs(self.nums[i] - self.nums[i+1]))
        return min([absoluteDiff(root.left, li, mid), absoluteDiff(root.right, mid+1, ri), combined])

    return absoluteDiff(self.root, left, right)


class Solution:
  def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    ans = []
    tree = SegmentTree(nums)
    for q in queries:
      ans.append(tree.absDifference(q[0], q[1]))
    return ans



# ans = [-1,1,1,3]
nums = [4,5,2,2,7,10]
queries = [[2,3],[0,2],[0,5],[3,5]]
Solution().minDifference(nums, queries)