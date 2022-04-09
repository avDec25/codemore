from typing import List

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    self.all_subsets = []
    self.backtrack([], nums, 0)
    return self.all_subsets
  
  def backtrack(self, tempset, nums, i):
    self.all_subsets.append(tempset.copy())
    for k in range(i, len(nums)):
      tempset.append(nums[k])
      self.backtrack(tempset, nums, k+1)
      tempset.pop()      

nums = [1,2,3]
print(Solution().subsets(nums))