from codemore.lowestCommonAncestor import TreeNode, generateTree


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        def pathSum(root, flowingSum) -> bool:
            if root.left is None and root.right is None:
                return (root.val + flowingSum) == targetSum

            l = pathSum(root.left,  flowingSum + root.val) if root.left else False
            r = pathSum(root.right,  flowingSum + root.val) if root.right else False
        
            return l or r

        return pathSum(root, 0)
        

tree = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 27
root = generateTree(tree, 0)
Solution().hasPathSum(root, targetSum)
