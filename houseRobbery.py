from typing import List

class Solution:  
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0
    
    p1 = 0
    p2 = 0
    
    for x in nums:
      tmp = p1
      p1 = max(p2 + x, p1)
      p2 = tmp
    
    return p1

nums = [1, 3, 1]
print(Solution().rob(nums))
