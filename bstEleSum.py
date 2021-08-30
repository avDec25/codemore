# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from codemore.lowestCommonAncestor import TreeNode, generateTree

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def containsSum(root, sm):
            if not root: return False
            if (k - root.val) in s: return True
            s.add(root.val)
            return containsSum(root.left, sm) or containsSum(root.right, sm)
        return containsSum(root, k)

root = [2, 1, 3]
k = 4
Solution().findTarget(generateTree(root), k)