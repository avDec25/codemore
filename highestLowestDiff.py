from typing import List
import math

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = math.inf
        for i in range((n - k) + 1):
            curSeqDiff = nums[i + k - 1] - nums[i]
            res = min(res, curSeqDiff)
        
        return res

nums = [90]
k = 1

nums = [9,4,1,7]
k = 2
Solution().minimumDifference(nums, k)