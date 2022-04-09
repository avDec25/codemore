from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                res += dp[(j, diff)]
                dp[(i,diff)] += dp[(j,diff)] + 1
        return res

nums = [2,4,6,8,10]
Solution().numberOfArithmeticSlices(nums)
