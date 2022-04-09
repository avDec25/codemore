from typing import List


class Solution:
    def findAll2Sum(self, nums, i, target):
        result = set()
        px = i+1
        py = len(nums)-1
        while px < py:
            sum2 = nums[px] + nums[py]
            if sum2 == target:
                # tuples are hashable hence can be a part of a set.
                # this is in contrast to an array
                # All immutable(which cannot be changed) built-in objects in Python are hashable like tuples
                result.add((nums[px], nums[py]))
                px = px + 1
                py = py - 1
            elif sum2 > target:
                py = py-1
            else:
                px = px+1

        return set() if len(result) == 0 else result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            # if new element is same as the previous element then try with a new element value instead
            # coz it would have been included already in a solution
            if i > 0 and nums[i-1] == nums[i]:
                continue
            t_sum = -nums[i]
            allPairs = self.findAll2Sum(nums, i, t_sum)
            for pair in allPairs:
                result.append([nums[i], pair[0], pair[1]])

        return result


nums = [-2, 0, 1, 1, 2]
print(Solution().threeSum(nums))
