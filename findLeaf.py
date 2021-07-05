from codemore.lowestCommonAncestor import Solution, TreeNode, generateTree, preOrder
from typing import List

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ans = []
        
        

tree = [1, 2, 3, 4, 5]
root = generateTree(tree)
Solution().findLeaves(root)