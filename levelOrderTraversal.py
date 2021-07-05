from typing import List
from codemore.lowestCommonAncestor import TreeNode, generateTree


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        level = [root]
        while root and level:
            current_nodes = []
            next_level = []
            for node in level:
                current_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            ans.append(current_nodes)
            level = next_level
        return ans


tree = ['f', 'b', 'g', 'a', 'd', None, 'i', None, None, 'c', 'e', None, None, 'h', None]
root = generateTree(tree, 0)
Solution().levelOrder(root)
