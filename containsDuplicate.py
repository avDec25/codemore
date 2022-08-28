# containsDuplicate.py
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for e in nums:
            if e not in seen:
                seen.add(e)
            else:
                return True
        return False

nums = [1,1,1,3,3,4,3,2,4,2]
Solution().containsDuplicate(nums)