from typing import List

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    self.all_permutations = []
    self.backtrack([], nums)
    return self.all_permutations

  def backtrack(self, templist, nums):
    if len(templist) == len(nums):
      self.all_permutations.append(templist.copy())
    else:
      for i in range(len(nums)):
        if nums[i] in templist: continue
        templist.append(nums[i])
        self.backtrack(templist, nums)
        templist.pop()

nums = [1, 2, 3]
Solution().permute(nums)