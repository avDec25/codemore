from typing import List

#%%
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = ( left + right ) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid+1

        return -1

nums = [5]
target = 0
Solution().search(nums, target)



# %%

class Solution:
    def isBadVersion(self, version) -> bool:
        return version >= 4

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


n = 5
Solution().firstBadVersion(n)

# %%
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

nums = [1, 3, 5, 6]
target = 5
Solution().searchInsert(nums, target)
# %%
