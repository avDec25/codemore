from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
      return []
    
    q = collections.deque()
    visited = {}    
    nodeOnLevel = {}
    
    q.append([root, 0])
    visited[root] = True
    while len(q) > 0:
      front = q.popleft()
      node = front[0]
      level = front[1]
      nodeOnLevel[level] = nodeOnLevel.get(level, []) + [node.val]
      
      if node.left and not visited.get(node.left, False):
        q.append([node.left, level+1])
        visited[node.left] = True
        
      if node.right and not visited.get(node.right, False):
        q.append([node.right, level+1])
        visited[node.right] = True
    
    print(nodeOnLevel)
    return [x for x in nodeOnLevel.values()]
      
    
