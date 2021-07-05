# Subarray Sums Divisible by K
from typing import List

class Solution:
    def subarraysDivByK(self, a: List[int], k: int) -> int:
        cumm_sum = 0
        sum_remainder = { 0: 1 }
        ans = 0
        for x in a:
            cumm_sum = (cumm_sum + x) % k
            ans += sum_remainder.get(cumm_sum, 0)
            sum_remainder[cumm_sum] = sum_remainder.get(cumm_sum, 0) + 1
        return ans

nums = [4, 5, 0, -2, -3, 1]
k = 5
Solution().subarraysDivByK(nums, k)
