from typing import List

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    tortoise = nums[0]
    hare = nums[0]

    while True:
      tortoise = nums[tortoise]
      hare = nums[nums[hare]]
      if tortoise == hare:
        break

    tortoise = nums[0]
    while tortoise != hare:
      tortoise = nums[tortoise]
      hare = nums[hare]
    return hare

nums = [3, 1, 3, 4, 2]
Solution().findDuplicate(nums)
