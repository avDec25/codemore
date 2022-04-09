from typing import List


class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    prod = 1
    zc = 0
    for e in nums:
      if e == 0:
        zc = zc + 1
        if zc > 1: break
      else:
        prod = prod * e

    if zc > 1:
      return [0 for _ in range(len(nums))]

    if zc == 0:
      return [prod//nums[i] for i in range(len(nums))]

    return [prod if e==0 else 0 for e in nums]

nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))
