# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, l=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from lowestCommonAncestor import TreeNode, generateTree

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        total = 0
        def sm(root):
            if not root: return 0
            l, r = sm(root.left), sm(root.right)
            self.res = max(self.res, l*(total-l), r * (total-r))
            return l+r+root.val
        total = sm(root)
        sm(root)
        return self.res % (10**9 + 7)

root = [2,3,9,10,7,8,6,5,4,11,1]
root = generateTree(root, 0)
Solution().maxProduct(root)