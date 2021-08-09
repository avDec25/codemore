from codemore.lowestCommonAncestor import TreeNode, generateTree, preOrder
from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        rev_index = dict()

        for i, v in enumerate(inorder):
            rev_index[v] = i

        root = TreeNode(val=postorder[-1])
        for p in postorder[-2::-1]:
            p_index = rev_index[p]
            ptr = root
            while ptr:
                curr_index = rev_index[ptr.val]
                if curr_index < p_index:
                    if ptr.right is None:
                        ptr.right = TreeNode(val=p)
                        break
                    else:
                        ptr = ptr.right
                else:
                    if ptr.left is None:
                        ptr.left = TreeNode(val=p)
                        break
                    else:
                        ptr = ptr.left
        return root

inorder   = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
Solution().buildTree(inorder, postorder)
