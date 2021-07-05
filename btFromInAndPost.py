from codemore.lowestCommonAncestor import TreeNode, generateTree, preOrder
from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
Solution().buildTree(inorder, postorder)
