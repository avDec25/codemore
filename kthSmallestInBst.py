# Kth Smallest Element in a BST
class TreeNode:
  def __init__(self, val=0, left=None, right=None):    
    self.val = val
    self.left = left
    self.right = right
  
  def __repr__(self) -> str:
    return f"node({self.val})"

class Solution:
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    def inorderTraversal(node, inOrder):
      if not node:
        return
      inorderTraversal(node.left, inOrder)
      inOrder.append(node.val)
      inorderTraversal(node.right, inOrder)

    inOrder = []
    inorderTraversal(root, inOrder)
    print(inOrder)
    return inOrder[k-1]

def generateTree(a, i) -> TreeNode:
  if i >= len(a) or a[i] is None:
    return None
  root = TreeNode(val=a[i])
  root.left = generateTree(a, 2*i+1)
  root.right = generateTree(a, 2*i+2)
  return root

def preOrder(root: TreeNode):
  if root is not None:
    print(root, end=", ")
    preOrder(root.left)
    preOrder(root.right)

#       0 1 2 3 4 5    6    7
tree = [5,3,6,2,4,None,None,1]
k = 3
root = generateTree(tree, 0)
Solution().kthSmallest(root, k)