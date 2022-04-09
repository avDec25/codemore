from typing import List

class Solution:
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    self.all_subsets = []
    nums.sort()
    self.backtrack([], nums, 0)
    return self.all_subsets
  
  def backtrack(self, templist, nums, i):
    self.all_subsets.append(templist.copy())
    for k in range(i, len(nums)):
      # Skip duplicates, look at it as 
      # Suppose 1 is added Then 1 again is added if that is the next element in the sorted array
      if k > i and nums[k] == nums[k-1]: continue

      templist.append(nums[k])
      self.backtrack(templist, nums, k+1)
      templist.pop()

nums = [1, 1, 2]
ans = Solution().subsetsWithDup(nums)
print(ans)