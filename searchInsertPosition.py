from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def condition(x):
            return nums[x] >= target

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid+1
        return left

        
nums = [1,3,5,6]
target = 5
Solution().searchInsert(nums, target)
