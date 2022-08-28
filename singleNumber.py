#%%
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        missing = nums[0]
        for i in range(1, len(nums)):
            missing ^= nums[i]
        return missing

nums = [4,1,2,1,2]
Solution().singleNumber(nums)

# %%
