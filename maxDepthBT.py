from codemore.lowestCommonAncestor import TreeNode, generateTree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(root) -> int:
            if root:
                if root.left is None and root.right is None:
                    return 1
                else:
                    return 1 + max(depth(root.left), depth(root.right))
            else:
                return 0

        return depth(root)


tree = [3, 9, 20, None, None, 15, 7]
root = generateTree(tree, 0)
Solution().maxDepth(root)
