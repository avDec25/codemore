from typing import List
from functools import cmp_to_key

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(nums, key=int)
        return nums[-k]

nums = ["3", "6", "7", "10"]
k = 4
Solution().kthLargestNumber(nums, k)