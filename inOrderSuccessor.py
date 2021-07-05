from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"node({self.val})"


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans = None
        while root:
            if p.val < root.val:
                ans = root
                root = root.left
            else:
                root = root.right
        return ans


class Solution2:
    def inorderSuccessorNaive(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None or p is None:
            return None
        queue = deque([])
        node = root
        while node or queue:
            while node:
                queue.appendleft(node)
                node = node.left
            node = queue.popleft()
            if node == p:
                ans = node.right
                while ans and ans.left:
                    ans = ans.left
                if ans is None:
                    ans = queue.popleft() if len(queue) > 0 else None
                    return ans
                if node.right:
                    queue.append(node.right)
            else:
                node = node.right
        return None

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor


def generateTree(a, i) -> TreeNode:
    if i >= len(a) or a[i] is None:
        return None
    root = TreeNode(val=a[i])
    root.left = generateTree(a, 2 * i + 1)
    root.right = generateTree(a, 2 * i + 2)
    return root


tree = [5, 3, 6, 2, 4, None, None, 1]
p = 5
root = generateTree(tree, 0)
ans = Solution().inorderSuccessor(root, p)
print(ans)