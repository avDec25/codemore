from typing import List
import math

class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    i, j, sum, minLen, n = 0, 0, 0, math.inf, len(nums)
    while j < n:
      sum += nums[j]
      j += 1
      
      while sum >= target:
        minLen = min(minLen, j-i)
        sum -= nums[i]
        i += 1

    if math.isinf(minLen):
      return 0
    else:
      return minLen

target = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(target, nums))
