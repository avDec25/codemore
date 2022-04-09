from typing import List

class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    self.all_permutations = []
    nums.sort()
    self.used = [False for _ in range(len(nums))]
    self.backtrack([], nums)
    return self.all_permutations
  
  def backtrack(self, templist, nums):
    if len(templist) == len(nums):
      self.all_permutations.append(templist.copy())

    for i in range(len(nums)):
      if self.used[i] or i > 0 and nums[i] == nums[i-1] and not self.used[i-1]: continue
      self.used[i] = True
      templist.append(nums[i])
      self.backtrack(templist, nums)
      templist.pop()
      self.used[i] = False

nums = [1, 2, 2]
print(Solution().permuteUnique(nums))