from typing import List

class Solution:
  def minMoves2(self, nums: List[int]) -> int:
    nums = sorted(nums)
    toBe = nums[len(nums) // 2]
    ans = 0
    for k in nums:
      ans += abs(k-toBe)    
    return ans

nums = [1,2,3]
print(Solution().minMoves2(nums))
