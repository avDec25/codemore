from typing import List


class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    n = len(nums)
    cummSum = [0] * n
    for i,v in enumerate(nums):
      cummSum[i] += nums[i] + (cummSum[i-1] if i-1 >= 0 else 0)
    
    for i in range(n):
      leftSum = cummSum[i-1] if i-1 >= 0 else 0
      rightSum = cummSum[n-1] - cummSum[i]
      if rightSum == leftSum:
        return i
      
    return -1

nums = [1, 7, 3, 6, 5, 6]
print(Solution().pivotIndex(nums))
