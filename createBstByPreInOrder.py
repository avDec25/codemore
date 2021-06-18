from typing import List
import copy

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    iMap = dict()
    for i, v in enumerate(inorder):
      iMap[v] = i
    ans = TreeNode(val=preorder[0])

    def insertInto(tree, x):
      if tree is None:
        return
      
      p = tree
      while p:
        if p.left == None and iMap[x] < iMap[p.val]:
          p.left = TreeNode(val=x)
        if p.right == None and iMap[x] > iMap[p.val]:
          p.right = TreeNode(val=x)

        if iMap[x] < iMap[p.val]:
          p = p.left
        else:
          p = p.right

    for e in preorder:
      if e != preorder[0]:
        insertInto(ans, e)
    return ans

preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
tree = Solution().buildTree(preorder, inorder)


def preOrder(tree: TreeNode):
  if not tree:
    return
  print(tree.val)
  preOrder(tree.left)
  preOrder(tree.right)
print("Tree Order Traversal:")
preOrder(tree)