from typing import List

class Solution:
  def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
    ans, dp = 0, 0
    prev = -1
    for i in range(len(nums)):
      if nums[i] < left:
        pass
      if right < nums[i]:
        dp = 0
        prev = i
      if left <= nums[i] <= right:
        dp = i - prev
      ans += dp
    return ans

nums = [2, 1, 4, 3]
left = 2
right = 3
Solution().numSubarrayBoundedMax(nums, left, right)
