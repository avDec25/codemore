# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lowestCommonAncestor import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodN(root, mx):
            if not root: return 0
            ans = 1 if root.val >= mx else 0
            ans += goodN(root.left, max(root.val, mx))
            ans += goodN(root.right, max(root.val, mx))
            return ans
        return goodN(root, -20000)