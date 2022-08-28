#%%
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        i3 = 0
        nums = [0] * (m+n)
        while i1 < m and i2 < n:
            if nums1[i1] <= nums2[i2]:
                nums[i3] = nums1[i1]
                i1 += 1
            else:
                nums[i3] = nums2[i2]
                i2 += 1
            i3 += 1

        while i1 < m:
            nums[i3] = nums1[i1]
            i1 += 1
            i3 += 1

        while i2 < n:
            nums[i3] = nums2[i2]
            i2 += 1
            i3 += 1
            
        for i in range(m+n):
            nums1[i] = nums[i]


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)

# %%
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast: 
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


# head = [3, 2, 0, -4]
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next = head.next

# pos = 1
head = head.next
Solution().hasCycle(head)

# %%
# Min Stack
# Design a stack that supports push, pop, top, and retrieving 
# the minimum element in constant time.
# Implement the MinStack class:
# ============================
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        stkMin = self.getMin()
        if stkMin == None or stkMin > val:
            self.stk.append((val, val))
        else:
            self.stk.append((val, stkMin))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        if self.stk == None:
            return None
        return self.stk[-1][0]

    def getMin(self) -> int:
        if len(self.stk) == 0:
            return None
        return self.stk[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# %%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        posA = headA
        lenA = 0
        while posA != None:
            posA = posA.next
            lenA += 1

        posB = headB
        lenB = 0
        while posB != None:
            posB = posB.next
            lenB += 1

        posA = headA
        posB = headB
        diff = lenA - lenB
        if diff > 0:
            while diff != 0:
                posA = posA.next
                diff -= 1
        else:
            while diff != 0:
                posB = posB.next
                diff += 1

        while posA != None and posB != None:
            if posA == posB:
                return True
            posA = posA.next
            posB = posB.next
        
        return False
    
    
# %%
# Excel Sheet Column Number
import math
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        faceValue = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26,
        }
        result = 0
        for index, character in enumerate(columnTitle[::-1]):
            result += faceValue[character] * math.pow(26, index)

        return int(result)

columnTitle="AB"
Solution().titleToNumber(columnTitle)
# %%
# Missing Ranges

from typing import (
    List,
)

class Solution:
    def find_missing_ranges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        n = len(nums)

        result = []
        for i in range(n-1):
            self.append_range(nums, result, i)

        n = len(nums)
        if n != 0:
            if lower < nums[0]:
                if lower == nums[0]-1:
                    result.insert(0, f"{lower}")
                else:
                    result.insert(0, f"{lower}->{nums[0]-1}")
            if nums[n-1] < upper:
                if upper == nums[n-1]+1:
                    result.append(f"{upper}")
                else:
                    result.append(f"{nums[n-1]+1}->{upper}")
        else:
            if lower == upper:
                result.append(str(lower))
            else:
                result.append(f"{lower}->{upper}")

        return result

    def append_range(self, nums, result, i):
        print(f"applied range, {i}")
        l = nums[i]+1
        r = nums[i+1]-1
        if l == r:
            result.append(f"{l}")
        elif l < r:
            result.append(f"{l}->{r}")

nums = [1,2,3,4,5,6,7,8]
lower = 1
upper = 9
Solution().find_missing_ranges(nums, lower, upper)
# %%
