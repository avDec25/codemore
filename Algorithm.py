#%%
# Binary Search
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1


nums = [12]
target = 12
Solution().search(nums, target)
# %%
# First Bad Version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def isBadVersion(self, version: int) -> bool:
        return version >= 4

    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            if self.isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l


n = 5
Solution().firstBadVersion(n)
# %%
# Search Insert Position
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid
            elif nums[mid] < target:
                l = mid+1
        return l+1 if nums[l] < target else l


nums = [1, 3, 5, 6]
target = 2
Solution().searchInsert(nums, target)
# %%
