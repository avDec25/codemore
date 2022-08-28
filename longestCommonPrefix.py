#%%
class Solution:
    def longestCommonPrefix(self, m):
        s1 = min(m)
        s2 = max(m)
        print(s1)
        print(s2)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s2[:i]
        return s1

strs = ["dog","racecar","car"]
Solution().longestCommonPrefix(strs)
# %%
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        x = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x += 1
            print(nums)
        return x

nums = [0,0,1,1,1,2,2,3,3,4]
Solution().removeDuplicates(nums)    
# %%
# substring within another string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1

haystack = "hello"
needle = "ll"
Solution().strStr(haystack, needle)

# %%
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        nums1[:n] = nums2[:n]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
# %%
