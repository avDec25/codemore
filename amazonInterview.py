#%% 
# Two Sum
from typing import List
class Solution:
    # https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, e in enumerate(nums):
            remainder = target - e
            if remainder in seen:
                return [seen[remainder], i]
            else:
                seen[e] = i

nums = [3,2,4]
target = 6
Solution().twoSum(nums, target)
# %% 
# Robot Bounded In Circle
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == "R": dx, dy = dy, 