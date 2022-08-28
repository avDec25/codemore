#%%
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        p = 1

        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]

        p = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output


nums = [-1,1,0,-3,3]
Solution().productExceptSelf(nums)

# %%
