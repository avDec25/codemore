#%% 
# Running Sum 1d Array
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        r_sum = 0
        for e in nums:
            r_sum += e
            result.append(r_sum)
        return result

nums = [1,2,3,4]
Solution().runningSum(nums)
# %%
# 724. Find Pivot Index
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        l_sum = [0] * n
        r_sum = [0] * n
        for i in range(n-2, -1, -1):
            r_sum[i] = r_sum[i+1] + nums[i+1]
        for i in range(1, n):
            l_sum[i] = l_sum[i-1] + nums[i-1]
            
        for i in range(n):
            if r_sum[i] == l_sum[i]:
                return i
        return -1

nums = [-1,-1,0,0,-1,-1]
Solution().pivotIndex(nums)


# %%
# 205. Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # replace each character in string with the first
        # index at which it appears
        # 
        for c in s:
            print(s.find(c))
        print(list(map(s.find, s)))
        print(list(map(t.find, t)))
        return list(map(s.find, s)) == list(map(t.find, t))

s = "eggpppkk"
t = "addqqqrr"
Solution().isIsomorphic(s, t)


# %%
#  Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) <= len(t):
            si = 0
            for i in range(len(t)):
                if t[i] == s[si]:
                    si += 1
                if si == len(s):
                    return True
        return False

s = "abc"
t = "ahbgdc"
Solution().isSubsequence(s, t)
# %%
# Merge Two Sorted Lists
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        result = ""
        head = self
        while head:
            result += f"{head.val} -> "
            head = head.next
        return result

# to be solved using dummy nodes and initialize current also as dummy
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2
        
        if list1 or list2:
            curr.next = list1 if list1 else list2
        
        return dummy.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print(list1)
print(list2)
Solution().mergeTwoLists(list1, list2)
# %%
# Reverse a Linked List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        result = ""
        head = self
        while head:
            result += f"{head.val} -> "
            head = head.next
        return result
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p, q, r = None, head, head.next
        while r:
            q.next = p
            p, q, r = q, r, r.next
        q.next = p
        p = q
        return p

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
Solution().reverseList(head)

# %%
# Middle of the Linked List
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
Solution().middleNode(head)

#%% 
# 142. Linked List Cycle II
from typing import Optional
from time import sleep

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return f"{self.val} -> "

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
           slow, fast = slow.next, fast.next.next
           if slow == fast: break
        else: return None
        while head != slow:
            head, slow = head.next, slow.next
        return head

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
Solution().detectCycle(head)

# %%
# Best Time to Buy and Sell Stock
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        result = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                result = max(result, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return result

prices = [7, 1, 5, 3, 6, 4]
Solution().maxProfit(prices)

# %%
# 409. Longest Palindrome
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        one_flag = 0
        palin = 0
        for e in counts:
            if counts[e] & 1:
                one_flag = 1
                palin += counts[e] - 1
            else:
                palin += counts[e]
        return palin + one_flag

s="abccccdd"
Solution().longestPalindrome(s)
# %%
# N-ary Tree Preorder Traversal
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
    def __repr__(self):
        return f"{self.val}"

class Solution:
    def pre_order(self, root):
        if root:
            self.q.append(root.val)
            if root.children:
                for c in root.children:
                    self.pre_order(c)

    def preorder(self, root: 'Node') -> List[int]:
        self.q = []
        self.pre_order(root)
        return self.q

n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n3.children = [n5, n6]
n2 = Node(2)
n1 = Node(1)
n1.children = [n3, n2, n4]
root = n1
Solution().preorder(root)

# %%
# Binary Tree Level Order Traversal
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"{self.val}"

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans

n9 = TreeNode(9)
n15 = TreeNode(15)
n7 = TreeNode(7)

n20 = TreeNode(20)
n20.left = n15
n20.right = n7

n3 = TreeNode(3)
n3.left = n9
n3.right = n20
Solution().levelOrder(n3)

# %%
# Binary Search
# correct binary search implementation
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right: # this also means that array with 1 element is taken care of
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

nums = [2, 5]
target = 5
Solution().search(nums, target)

# %%
# first bad version
class Solution:
    def isBadVersion(self, version: int) -> bool:
        return version == 4

    def firstBadVersion(self, n: int) -> int:
        ans = -1
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans

n = 5
Solution().firstBadVersion(n)

# %%
# Validate Binary Search Tree
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"{self.val}"

class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor=float('-inf'), ceiling=float('inf')) -> bool:
        if not root: return True
        if floor >= root.val or root.val >= ceiling:
            return False
        return self.isValidBST(root.left, floor, root.val) and \
            self.isValidBST(root.right, root.val, ceiling)
        

n5 = TreeNode(5)
n1 = TreeNode(1)
n4 = TreeNode(4)
n3 = TreeNode(3)
n6 = TreeNode(6)

n4.left = n3
n4.right = n6
n5.left = n1
n5.right = n4
Solution().isValidBST(n5)

# %%
# 235. Lowest Common Ancestor of a Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.val}"

class Solution:
    def pre_order(self, root: 'TreeNode'):
        if root:
            print(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

n0 = TreeNode(0)
n3 = TreeNode(3)
n5 = TreeNode(5)
n7 = TreeNode(7)
n9 = TreeNode(9)
n4 = TreeNode(4)
n2 = TreeNode(2)
n8 = TreeNode(8)
n6 = TreeNode(6)
n6.left  = n2
n6.right = n8
n2.left  = n0
n2.right = n4
n4.left  = n3
n4.right = n5
n8.left  = n7
n8.right = n9
# Solution().lowestCommonAncestor(n6, n2, n8)
Solution().lowestCommonAncestor(n6, n2, n4)
# Solution().lowestCommonAncestor(n6, n7, n4)
# %%
# 733. Flood Fill
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n_row = len(image)
        n_col = len(image[0])
        visited = set()
        q = [(sr, sc)]
        visited.add((sr,sc))
        to_replace = image[sr][sc]
        while q:
            x, y = q.pop(0)
            image[x][y] = color
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_x , new_y = x + dx, y + dy
                if -1 < new_x < n_row and -1 < new_y < n_col \
                    and (new_x, new_y) not in visited \
                    and image[new_x][new_y] == to_replace:
                    q.append((new_x, new_y))
                    visited.add((new_x, new_y))
        return image
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 0
color = 2
Solution().floodFill(image, sr, sc, color)

# %%
# 200. Number of Islands
class Solution:
    def bfs(self, grid, r, c):
        R = len(grid)
        C = len(grid[0])
        q = [(r,c)]
        self.visited.add((r,c))
        while q:
            x, y = q.pop(0)
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                new_x, new_y = dx+x, dy+y
                if -1 < new_x < R and -1 < new_y < C \
                    and (new_x, new_y) not in self.visited \
                    and grid[new_x][new_y] == "1":
                    q.append((new_x, new_y))
                    self.visited.add((new_x, new_y))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n_row = len(grid)
        n_col = len(grid[0])
        self.visited = set()
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == "1" and (r,c) not in self.visited:
                    ans += 1
                    self.bfs(grid, r, c)
        return ans

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Solution().numIslands(grid)

# %%
# 509. Fibonacci Number
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n <= 1: return n
        else:
            return self.fib(n-1) + self.fib(n-2)

n = 30
Solution().fib(n)
# %%
# 70. Climbing Stairs
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

n = 5
Solution().climbStairs(n)

# %%
# 746. Min Cost Climbing Stairs
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = 0
        
        return ans
    
cost = [1,100,1,1,1,100,1,1,100,1]
Solution().minCostClimbingStairs(cost)

# %%
