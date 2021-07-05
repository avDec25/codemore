# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):    
        self.val = val
        self.left = left
        self.right = right
  
    def __repr__(self) -> str:
        return f"node({self.val})"


def generateTree(a, i=0) -> TreeNode:
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

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(root, p, q):
            if root is None:
                return None
            if root.val == p or root.val == q:
                return root
            
            leftNode  = lca(root.left, p, q)
            rightNode = lca(root.right, p, q)

            if leftNode and rightNode:  
                return root
            
            return (rightNode if leftNode is None else leftNode)
        
        return lca(root, p, q)


    #   0  1  2  3  4  5  6  7     8     9  10
tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 4
root = generateTree(tree, 0)
Solution().lowestCommonAncestor(root, p, q)