# Subarray Sums Equals by K
from typing import List


class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        cumm_sum = 0
        pre_sum = {0: 1}
        ans = 0
        for x in a:
            cumm_sum += x
            ans += pre_sum.get(cumm_sum-k, 0)
            pre_sum[cumm_sum] = pre_sum.get(cumm_sum, 0) + 1
        return ans


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
Solution().subarraySum(nums, k)
