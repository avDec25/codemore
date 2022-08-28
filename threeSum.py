#%%
from typing import List

#%%
class Solution:
    def twoSum(self, nums, i, target):
        result = set()
        px = i+1
        py = len(nums)-1
        while px < py:
            sum2 = nums[px] + nums[py]
            if sum2 == target:
                result.add((nums[px], nums[py]))
                px += 1
                py -= 1
            elif sum2 > target:
                py -= 1
            else:
                px += 1
        return set() if len(result) == 0 else result


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            t_sum = -nums[i]
            allPairs = self.twoSum(nums, i, t_sum)
            for pair in allPairs:
                result.append([nums[i], pair[0], pair[1]])

        return result

nums = [-1,0,1,2,-1,-4]
Solution().threeSum(nums)
# %%
