# Populating Next Right Pointers in Each Node
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.val})"


def generateTree(a, i):
    if i >= len(a) or a[i] is None:
        return None

    root = Node(val=a[i])
    root.left  = generateTree(a, 2*i+1)
    root.right = generateTree(a, 2*i+2)
    return root


def preOrder(root: Node):
    if root is not None:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        


tree = [1, 2, 3, 4, 5, 6, 7]
root = generateTree(tree, 0)
Solution().connect(root)
