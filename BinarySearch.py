# %%
from typing import List
from typing import Optional

# %%
# Evaluate Boolean Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        def preorder(root: Optional[TreeNode]):
            if root:
                self.ans += f"{root.val}, "
                preorder(root.left)
                preorder(root.right)

        self.ans = ""
        preorder(root)
        return self.ans


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)

        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)

        return root.val == 1


# root = [2,1,3,null,null,0,1]
root = TreeNode(2)
rl = TreeNode(1)
rr = TreeNode(3)
rrl = TreeNode(0)
rrr = TreeNode(1)
root.left = rl
root.right = rr
root.right.left = rrl
root.right.right = rrr
Solution().evaluateTree(root)
# %%
# Find Target Indices After Sorting Array


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lt_count, eq_count = 0, 0
        for i in nums:
            if i == target:
                eq_count += 1
            elif i < target:
                lt_count += 1
        return list(range(lt_count, lt_count+eq_count))


nums = [1, 2, 5, 2, 3]
target = 5
Solution().targetIndices(nums, target)
# %%
# Count Negative Numbers in a Sorted Matrix


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, ans = 0, n-1, 0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                ans += m-r
                c -= 1
            else:
                r += 1
        return ans


grid = [[4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]]
Solution().countNegatives(grid)

# %%
# The K Weakest Rows in a Matrix


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        rows = sorted(range(m), key=lambda i: (mat[i], i))
        return rows[:k]


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3
Solution().kWeakestRows(mat, k)

# %%
# Intersection of Two Arrays


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return list(set(nums1) & set(nums2))


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
Solution().intersection(nums1, nums2)
