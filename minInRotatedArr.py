from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        left, right = 0, n-1
        while left < right:
            mid = (right+left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


nums = [11, 13, 15, 17]
Solution().findMin(nums)