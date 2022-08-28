# %%
# Path Sum III
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"{self.val}"

class Solution:
    def pre_order(self, root: Optional[TreeNode]) -> None:
        if root:
            print(root)
            self.pre_order(root.left)
            self.pre_order(root.right)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        return 0

lll = TreeNode(3)
llr = TreeNode(-2)
lrr = TreeNode(1)
ll = TreeNode(3, lll, llr)
lr = TreeNode(2, None, lrr)
l = TreeNode(5, ll, lr)
rr = TreeNode(11)
r = TreeNode(-3, None, rr)
root = TreeNode(10, l, r)

targetSum = 8