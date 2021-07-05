from codemore.lowestCommonAncestor import generateTree, TreeNode


class Solution:
    def preOrder(self, root: TreeNode):
        ans = []
        def traverse(root: TreeNode):
            if root:
                ans.append(root.val)
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return ans

    def preOrderIterative(self, root: TreeNode):
        ans = []
        stk = list()
        stk.append(root)
        while len(stk) > 0:
            top = stk.pop()
            ans.append(top.val)
            if top.right:
                stk.append(top.right)
            if top.left:
                stk.append(top.left)
        return ans


tree = ['f', 'b', 'g', 'a', 'd', None, 'i', None, None, 'c', 'e', None, None, 'h', None]
root = generateTree(tree, 0)
Solution().preOrder(root)
Solution().preOrderIterative(root)
