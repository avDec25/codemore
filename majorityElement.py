#%%
from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums)//2
        data = Counter(nums)
        for e in data:
            if data[e] > target:
                return e
        return -1

nums = [2,2,1,1,1,2,2]
Solution().majorityElement(nums)
# %%
