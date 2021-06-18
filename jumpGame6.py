from typing import List
import collections


class Solution:
  def maxResult(self, nums: List[int], k: int) -> int:
    dq, n = collections.deque([0]), len(nums)
    for i in range(1, n):
      while dq and dq[0] < i-k:
        dq.popleft()
      
      nums[i] += nums[dq[0]]
      while dq and nums[i] >= nums[dq[-1]]:
        dq.pop()
      dq.append(i)
    return nums[-1]


nums = [1,-1,-2,4,-7,3]
k = 2
Solution().maxResult(nums, k)
