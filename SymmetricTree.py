# Given the root of a binary tree, 
# check whether it is a mirror of itself 
# (i.e., symmetric around its center).

from codemore.lowestCommonAncestor import TreeNode, generateTree

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        
        return isSym(root, root)


tree = [1,2,2,None,3,None,3]
root = generateTree(tree, 0)
Solution().isSymmetric(root)